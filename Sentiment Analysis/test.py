import _json
import csv
import json
import re

import tweepy

consumer_key = "ZLLDm9dd7MDd2pzJFA1Ip9QiD"
consumer_secret = "N64vO5EPOAAk7EUTIGqQ31iocVXks7m4DGpO66BDsmMwCTn3rO"
access_token = "1233487088466759681-pP9UqTy4uUgmFFYccAZRArzwM8wZIT"
access_token_secret = "dB7Olly73SGFz9R8gaLYnGdEL1rjL30s1WDv2UXRT03u0"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# passing keys to access the data

api = tweepy.API(auth, wait_on_rate_limit=True)
p1 = open("datatwitterr.csv", 'a', newline='', encoding="utf-8-sig")
p2 = csv.writer(p1)
data = ["created_at", "text", "User_Location", "lang", "retweeted", "reweet_count"]
p2.writerow(data)
for tweet in tweepy.Cursor(api.search,
                           q='Canada' or 'University' or 'Dalhousie University' or 'Halifax' or 'Canada Education').items(
        3010):
    data = []
    data.append(tweet._json["created_at"])
    # cleaning the data by attribute
    regex = re.sub(r'[^\x00-\x7F]+|http\S+', '', str(tweet._json["text"]))
    regex = [re.sub(r"[^a-zA-Z0-9]+", '', j) for j in regex.split(" ")]
    regex = " ".join(regex)
    data.append(regex)
    # appending each attribute after cleaning
    regex = re.sub(r'[^\x00-\x7F]+|http\S+', '', str(tweet._json["user"]["location"]))
    regex = [re.sub(r"[^a-zA-Z0-9]+", ' ', j) for j in regex.split(" ")]
    regex = " ".join(regex)
    data.append(regex)
    data.append(tweet._json["lang"])
    data.append(tweet._json["retweeted"])
    data.append(tweet._json["retweet_count"])
    p2.writerow(data)
