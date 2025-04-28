import json
from models import*
from utils import*
from reader import*
twiter_list=load_comments("twitter_data.json")


with open("special_characters.json", "r", encoding="utf-8") as file:
    special_characters = json.load(file) #עבודה על קובץ json

with open("negative_words.json", "r", encoding="utf-8") as file:
    negative_words = json.load(file)

with open("positive_words.json", "r", encoding="utf-8") as file:
    positive_words = json.load(file)


def old_list_toNew_dict(list: list)-> dict:
    comment_dict = {}
    for i in range(len(list)):
        temp_dict = list[i]
        if temp_dict["reply_to"] not in comment_dict: #אם המשתמש  לא נמצא במילון החדש
            comment_dict[temp_dict["reply_to"]] = [temp_dict["comment"]] #נייצר מפתח חדש במילון עם שם המתשמש והתגובה שהגיבו לו
        else: #במידה והמשתמש קיים כבר, נוסיף עוד תגובה לרשימת
            comment_dict[temp_dict["reply_to"]].append(temp_dict["comment"])
    return comment_dict

def analyze_sentiment(comment: Comment) -> str:
    stringi = comment.text.strip().split(" ") #לוקחת את הטקסט מהאויבקט ללא רווחים בהתחלה או בסוף ומפרידה בין המילים
    positive_count = 0
    negitive_count = 0
    for word in stringi: #עובר על כל מילה בטקסט
        if word in negative_words: #בודקת אם אותה מילה נממצאת ברשימת מילים השליליות ואם כן מוסיפה 1 לרשימה השלילית
            negitive_count +=1
        elif word in positive_words: #אותו הדבר עם מילים חיוביות
            positive_count += 1
    if positive_count > negitive_count:
        return "positive"
    elif negitive_count > positive_count:
        return "negative"
    else:
        return "neutral"



def find_short_comments(list: list)-> list: #מחפש תגובות בעלות פחות מ5 מילים
    short_list = []
    for i in range(len(list)):
        stringi = list[i]["comment"].strip() #לוקח כל פעם תגובה אחרת מהרשימה
        if stringi.count(" ") + 1 < 5: #אם בתגובה יש פחות מ5 מילים(+1 כי המערכת לא סופרת את המילה האחרונה בגלל שאין רווח)
            short_list.append(stringi)
    return short_list


def find_emoji(list: list)-> list:
    emoji_list = []
    for i in range(len(list)):
        for x in special_characters["special_characters"]:
            stat = fun_function(list[i]["comment"], x) #משתמשים בפונקציה לבדיקת אימוגי
            if stat == True:#אם אחרי הבידקה התגלה שיש אימוגי, נכניס לרשימה חדשה ונחזיר
                emoji_list.append(list[i]["comment"])
    return emoji_list

def comment_lengh(list: list):
    comment_sort_list=[]
    for i in range(len(list)):
        comment_stringi = list[i]["comment"]
        count_word = len(comment_stringi.strip().split(" "))
        comment_sort_list.append((count_word, comment_stringi))
    comment_sort_list.sort()
    return comment_sort_list

def most_positive_user(list:list):
    final_list = []
    data_base=load_comments("twitter_data.json")
    user_comments = {}
    for i in data_base:
        name = i["reply_to"]
        comment = i["comment"]
        if name not in user_comments:
            user_comments[name] = []
        user_comments[name].append(comment)
    for name, comments in user_comments.items():
        user = UserComments(name, comments)
        amount = user.positive_ratio()
        final_list.append((amount, name))
    final_list.sort()
    return final_list[-1][1]


def most_negative_user(list: list):
    final_list = []
    data_base = load_comments("twitter_data.json")
    user_comments = {}
    for i in data_base:
        name = i["reply_to"]
        comment = i["comment"]
        if name not in user_comments:
            user_comments[name] = []
        user_comments[name].append(comment)

    for name, comments in user_comments.items():
        user = UserComments(name, comments)
        amount = user.negative_ratio()
        final_list.append((amount, name))
    final_list.sort()
    return final_list[-1][1]


def longest_and_shortest(list:list):
    # list_minmax = []
    # for i in range(len(list)):
    #     comment = list[i]["comment"]
    #     count_of_words = len(comment.split(" "))
    #     list_minmax.append((count_of_words, comment))
    # list_minmax.sort()
    # print(f"the longest {list_minmax[0]}")
    # print(list_minmax[-1])
    list_minmax= comment_lengh(list)
    print(f"the shortest comment is: {list_minmax[0]}")
    print(f"the longest comment is: {list_minmax[-1]}")

print(most_negative_user(twiter_list))
