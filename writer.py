import json
from textwrap import indent

def result(myList:list):
    with open("C:/Users/eitanch/desktop/result.json",'a',encoding="utf-8") as file:
        for i in myList:
            json.dump(i,file,ensure_ascii=False,indent=4)