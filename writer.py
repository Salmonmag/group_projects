import json
from textwrap import indent

def result(myList:list):
        with open("data/result.json", 'a', encoding="utf-8") as file:
            try:
                for i in myList:
                    json.dump(i, file, ensure_ascii=False, indent=4)
            except TypeError as error:
                print(error)
            file.write(f"\n")
