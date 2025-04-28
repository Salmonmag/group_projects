from reader import *
from  models import *
from processor import *
from utils import *
from writer import *

# There is the extraction from the data file
comments_list = load_comments('twitter_data.json')
comments_object_list =list()
users_list = list()
#This loop creates a list of comments objects from the comments list stored into the comments_object_list
for i in comments_list:
    replyTo = i["reply_to"]
    comment = i['comment']
    comments_object_list.append(Comment(replyTo,comment))

#This loop creates a list of users objects stored into the users_list
dict_list = old_list_toNew_dict(comments_list).items()
for x in dict_list:
    username = x[0]
    hisComments = x[1]
    users_list.append(UserComments(username,hisComments))
sentimentResult = list()
for y in comments_object_list:
    sentimentResult.append(analyze_sentiment(y))

list_count_comments = list()
list_positive_ratio = list()
list_negative_ratio = list()
list_average_word_count = list()
for z in users_list:
    list_count_comments.append(z.count_comments())
    list_positive_ratio.append(z.positive_ratio())
    list_negative_ratio.append(z.negative_ratio())
    #list_average_word_count.append(z.average_word_count())

print(list_positive_ratio)
