import json
with open("special_characters.json", "r", encoding="utf-8") as file:
    special_characters = json.load(file) #עבודה על קובץ json

print(special_characters) #מדפיס את הקובץ כדי לראות את כל הסימנים


def clean(text: str):
    """פונקציה שמנקה תווים מיוחדים ואמוגים ומחזירה טקסט חדש"""
    clean_text = ""
    for sigh in text:
        if sigh not in special_characters['special_characters']:
            clean_text += sigh
    return clean_text

def fun_function(text: str):
    """בדיקה אם הטקסט מכיל אימוגים"""
    for f in text:
        for j in special_characters['special_characters']:
            if f == j:
                return True
    return False

def number_sigh(comment:str):
    """פונקציה שמחזירה את מספר סימני השאלה בתגובה"""
    question_sigh = 0
    for i in comment:
        if i == "?":
            question_sigh += 1
    return question_sigh

