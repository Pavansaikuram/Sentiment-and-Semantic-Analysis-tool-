import csv
import math

if __name__ == '__main__':
    import Semantic
    linecoun = Semantic.linecount
    print(linecoun)
outputfile = open(r"C:\Users\pavan\OneDrive\Documents\Semanticresults.csv", 'w', newline='')
csv_writer = csv.writer(outputfile)
adddata=["Total Documents",linecoun]
csv_writer.writerow(adddata)
adddata=["Search Query","Document containing term(df)","Total Documents(N)/number of documents term appeared(df)","Log(N/df)"]
csv_writer.writerow(adddata)

data = ["Canada", "University", "Dalhousie University", "Halifax", "Business"]
type(data)
listofart=[]
for list in data:
    adddata=[]
    adddata.append(list)
    print(list)
    doccount = 0
    z=0
    logvalue = 0
    for i in range(1, linecoun):
        with open("Semenatic" + str(i) + ".txt") as openfile:
            for line in openfile:
                if list in line:
                    doccount = doccount + 1
                    print(i)
                    if list == "Canada":
                        k = doccount
                        listofart.append(i)
    #print(doccount)
    #print(listofart)
    adddata.append(doccount)
    print("only canada count" + str(k))
    if doccount != 0:
        z = round((linecoun / doccount),2)
        #print(z)
        adddata.append(z)
        logvalue=round(math.log(z, 10),2)
        adddata.append(logvalue)
        #print(logvalue)
    csv_writer.writerow(adddata)
    print(adddata)
outputfile1 = open(r"C:\Users\pavan\OneDrive\Documents\Semanticres.csv", 'w', newline='')
csvwriter = csv.writer(outputfile1)
addrow=["Term","Canada"]
csvwriter.writerow(addrow)
addrow=["Canada appeared in "+str(k)+" Documents","Total word(m)","Frequency(f)"]
csvwriter.writerow(addrow)
hrf = 0
for i in listofart:
    addrow=[]
    with open("Semenatic" + str(i) + ".txt") as openfile:
        article=0
        canadacount = 0
        wordcount = 0
        for line in openfile:
            for part in line.split():
                wordcount = wordcount + 1
                if "Canada" in part:
                    article="Article #" + str(i)
                    canadacount = canadacount + 1
    addrow.append(article)
    addrow.append(wordcount)
    addrow.append(canadacount)
    csvwriter.writerow(addrow)
    print(addrow)

   # print(wordcount)
    if i == 1:
        print()
        hrf = (canadacount / wordcount)
        p=i
    else:
        if hrf < (canadacount / wordcount):
            hrf = (canadacount / wordcount)
            print("look here"+str(hrf))
            p=i
print("Look here" + str(hrf))
highest="Article with highest relative frequency is Article #" + str(p)
addhighest=[]
addhighest.append(highest)
csvwriter.writerow(addhighest)
