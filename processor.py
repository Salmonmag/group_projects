# twit_list= [{"reply_to": "@AndreCVentura", "comment": "Por isso que o Chega é  um partido de instabilidade e não estabilidade. Numa altura de responsabilidade e respeito pelos portugueses. Querem moções de censura e votam contra moção de confiança. "},
# {"reply_to": "@AndreCVentura", "comment": "Prepara-te para fazer as malas. Isto se ainda lá estiverem após as eleições "}]
# חשוב לשים לב!!!! התוכנה כרגע עובדת לפי הרשימה בשורות 1-2, צריך לעדכן אותה לקליטה מJSON
def processor(list: list)-> dict:
    comment_dict = {}
    for i in range(len(twit_list)):
        temp_dict = twit_list[i]
        if temp_dict["reply_to"] not in comment_dict: #אם המשתמש  לא נמצא במילון החדש
            comment_dict[temp_dict["reply_to"]] = [temp_dict["comment"]] #נייצר מפתח חדש במילון עם שם המתשמש והתגובה שהגיבו לו
        else: #במידה והמשתמש קיים כבר, נוסיף עוד תגובה לרשימת
            comment_dict[temp_dict["reply_to"]].append(temp_dict["comment"])
    return comment_dict


def find_short_comments(list: list):
    short_list = []
    for i in range(len(twit_list)): # עוברים כל םעם על שורה אחת מהרשימה
        stringi = twit_list[i]["comment"].strip() #בכל מילון שאנחנו בודקים, נהפוך את התגובה לSTR 
        if stringi.count(" ") + 1 < 5: #נבדוק את האורך של הרצועה, בעזרת ספירת הרווחים(+1) בשביל המילה האחרונה
            short_list.append(stringi) # מוסיפים כל פעם שורה חדשה אם נמצא שהיא קטנה מחמש
    return short_list
