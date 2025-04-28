import json
from textwrap import indent

def result(myList:list)->None:
    if type(myList) != list:
        return "Wrong type of attribute!"
    with open("C:/Users/eitanch/desktop/result.json",'a',encoding="utf-8") as file:
        for i in myList:
            json.dump(i,file,ensure_ascii=False,indent=4)
        file.write(f"\n")
