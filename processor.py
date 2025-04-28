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
    stringi = comment.text.strip().split(" ")
    positive_count = 0
    negitive_count = 0
    for word in stringi:
        if word in negative_words:
            negitive_count +=1
        elif word in positive_words:
            positive_count += 1
    if positive_count > negitive_count:
        return "positive"
    elif negitive_count > positive_count:
        return "negative"
    else:
        return "neutral"



def find_short_comments(list: list):
    short_list = []
    for i in range(len(list)):
        stringi = list[i]["comment"].strip()
        if stringi.count(" ") + 1 < 5:
            short_list.append(stringi)
    return short_list


def find_emoji(list: list)-> list:
    emoji_list = []
    for i in range(len(list)):
        for x in special_characters["special_characters"]:
            stat = fun_function(list[i]["comment"], x)
            if stat == True:
                emoji_list.append(list[i]["comment"])
    return emoji_list

def comment_lengh(list: list):
    comment_sort_list=[]
    for i in range(len(list)):
        comment_stringi = list[i]["comment"]
        count_word = len(list[i]["comment"])
        comment_sort_list.append((count_word, comment_stringi))
    comment_sort_list.sort()
    final_list = []
    for stringi in comment_sort_list:
        final_list.append(stringi[1])
    return final_list

def most_positive_user(list:list):
    update_dict = old_list_toNew_dict(list)
    user_scores = {}
    for user, comments in update_dict.items(): #עוברים על המילון ולוקחים את המפתח(שם) ורשימת התגובות
        total_score = 0
        for comment_text in comments: # עוברים על כל תגובה בנפרד בתוך הרשימת תגובות לכל משתמש
            comment_obj = Comment(user, comment_text) #לוקחים את הערכים שיש לנו והופכים אותו לאובייקט
            val = analyze_sentiment(comment_obj) # מכניסים את האוביקט שיש לנו לתוך הפונקציה בשביל לחשב אם התגובה חיובית או שלילית
            if val == "positive":
                total_score += 1 # אם התגובה חיובית מוספית למונה
            elif val == "negative":
                total_score -= 1 #אם שלילית מורידים מהמונה
        user_scores[user] = total_score #מכניסים למילון תוצאות שלנו את המשתמש(מפתח) והערך הוא הציון הסופי

    most_positive = max(user_scores, key=user_scores.get)
    return most_positive
test = most_positive_user(twiter_list)
print(test)
