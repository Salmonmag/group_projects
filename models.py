import json
from reader import *
with open("data/negative_words.json", "r", encoding="utf-8") as file:
  data_negative = json.load(file)
  # print(data_negative)

with open("data/positive_words.json", "r", encoding="utf-8") as file:
  data_positive = json.load(file)
  # print(data_positive)

class Comment:

    def __init__(self, reply_to:str, text:str):
        self.reply_to = reply_to
        self.text = text

    def word_count(self) ->int:
        """count how many words is in comment and save the number"""
        count_of_words = 0
        for word in self.text.split():
            count_of_words += 1
        return count_of_words

    def char_count(self)->int:
        """count how many chars is in comment and save the number"""
        count_of_chars = 0
        for char in range(len(self.text)):
            count_of_chars += 1
        return count_of_chars

class UserComments:

    def __init__(self, username, comments):
        self.username = username
        self.comments = comments

    def count_comments(self)->int:
        """count how many comments is in the file with comments and save the number"""
        count_comments = 0
        for comment in self.comments:
            count_comments += 1
        return count_comments

    def average_word_count(self)->int:
        """find the average number of words in each comment is in the file with comments and save the number"""
        temp_list = []
        for i in self.comments:
            temp_list.append(i.split(" "))
        return int(sum(temp_list)/len(temp_list))

    def positive_ratio(self)->int:
        """find if comment are positive or negative, and if it's positive, add this comment to count of positive words"""
        count_of_positive = 0
        reviewed_comments=self.comments.split(" ")
        for i in reviewed_comments:
            for j in data_positive:
                if i == j:
                    count_of_positive += 1
        return count_of_positive

    def negative_ratio(self)->int:
        """find if comment are positive or negative, and if it's negative, add this comment to count of negative words"""
        count_of_negative = 0
        reviewed_comments=self.comments.split(" ")
        for i in reviewed_comments:
            for j in data_negative:
                if i == j:
                    count_of_negative += 1
        return count_of_negative


