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
