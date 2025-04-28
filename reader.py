import json
#TODO: ליבא את כל הקבצים הרלוונטים
def load_comments(filepath:str)->list[dict]:
    """מוציאה את מילוני התגובות מקובץ ה twitter"""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            file_of_full_comments = file.readlines()
            list_for_users = []
        for comment in file_of_full_comments:
            list_for_users.append(json.loads(comment))
        return list_for_users

    except FileNotFoundError as error:
        print(error)
    except json.JSONDecodeError as error:
        print(error)

class CommentLoader:
    """מחזיר רשימה של כל התגובות ללא שמות משתמש בפורמט list"""

    def __init__(self,filepath:str):
        self.filepath=filepath

    def load(self)->list:
        list_of_full_comments = load_comments(self.filepath)
        list_of_individual_comments=[]

        for comment in list_of_full_comments:
            list_of_individual_comments.append(comment["comment"])

        return list_of_individual_comments

#יישום: from reader import load_comments,CommentLoader
