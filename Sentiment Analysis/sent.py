import csv

# Stored Tweets
inputfile = open(r"C:\Users\pavan\OneDrive\Documents\datatwitterchanged.csv", 'r')
# Output file of sentimental analysis
outputfile = open(r"C:\Users\pavan\OneDrive\Documents\Resultschange.csv", 'w', newline='')
csv_reader = csv.DictReader(inputfile)
csv_writer = csv.writer(outputfile)
# Adding Header to the output file
data = ["Tweet", "Message/tweets", "Match", "Polarity"]
csv_writer.writerow(data)
# Positive words text file
positivewords = open(r"C:\Users\pavan\OneDrive\Documents\Positivewords.txt", 'r')
# Negative words text file
negativewords = open(r"C:\Users\pavan\OneDrive\Documents\Negativewords.txt", 'r')
pos = []
neg = []
# for tweet count
i = 0
# Converting positive words to string
for line in positivewords:
    pos.append(line.rstrip('\n'))

# Converting negative words to string
for line in negativewords:
    neg.append(line.rstrip('\n'))

# Passing Each tweet to function
def word_count(tweet):
    Eachword = {}
    # print(Eachword)
    tweets = tweet.split()
    for word in tweets:
        if word in Eachword:
            Eachword[word] = Eachword[word] + 1
            # print(Eachword)
        else:
            Eachword[word] = 1
            # print(Eachword)
    return Eachword

# Taking tweets from csv file
for line in csv_reader:
    line["text"] = line["text"].replace("RT", "")
    i = i + 1
    data = []
    # For the tweet number
    data.append(i)
    data.append(line["text"])
    # passing to function
    word = word_count(line["text"])
    print(word)
    print(line["text"])
    word = word_count(line["text"])
    print(word)
    words = []
    x1 = 0
    y1 = 0
    for x in range(len(pos)):
        if pos[x] in word:
            words.append(pos[x])
            # positive words count
            x1 = x1 + word[pos[x]]

    for y in range(len(neg)):
        if neg[y] in word:
            words.append(neg[y])
            # Negative words count
            y1 = y1 + word[neg[y]]

    print(x1)
    print(y1)
    # converting list of match words to string
    matchwords = ','.join(words)
    print(matchwords)
    data.append(matchwords)
    if x1 > y1:
        print("positive word")
        data.append("Positive")
    elif x1 < y1:
        print("Negative word")
        data.append("Negative")
    else:
        print("Neutral")
        data.append("Neutral")
    print(data)
    # appending each row to csv file
    csv_writer.writerow(data)

# word=word_count('the quick abound brown fox jumps over the lazy dog.')
