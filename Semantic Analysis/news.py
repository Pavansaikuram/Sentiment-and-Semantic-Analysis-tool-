import csv
import json
import re

import requests
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='ce9309f140c4492bb3d41781f91c2e63')
p1 = open("datanewsss.csv", 'a', newline='', encoding="utf-8-sig")
p2 = csv.writer(p1)
# csv writer to write list of data to the csv file
data = ["Title", "Description", "Content"]
p2.writerow(data)


# adding headers to the csv file
def news(key):  # passing each key as a parameter to the function
    all_articles = newsapi.get_everything(q=key,
                                          language='en')
    print(all_articles)
    for x in all_articles["articles"]:
        data = []
        regex = re.sub(r'[^\x00-\x7F]+|http\S+', '', str(x["title"]))
        regex = [re.sub(r"[^a-zA-Z0-9]+", ' ', j) for j in regex.split(" ")]
        regex = " ".join(regex)
        data.append(regex)
        # cleaning each required attribute
        regex = re.sub(r'[^\x00-\x7F]+|http\S+', '', str(x["description"]))
        regex = [re.sub(r"[^a-zA-Z0-9]+", ' ', j) for j in regex.split(" ")]
        regex = " ".join(regex)
        data.append(regex)
        # appending attribute after cleaning
        regex = re.sub(r'[^\x00-\x7F]+|http\S+', '', str(x["content"]))
        regex = [re.sub(r"[^a-zA-Z0-9]+", ' ', j) for j in regex.split(" ")]
        regex = " ".join(regex)
        data.append(regex)
        p2.writerow(data)


news("Canada")
news("University")
news("Dalhousie University")
news("Halifax")
news("Canada Education")
news("Moncton")
news("Toronto")
