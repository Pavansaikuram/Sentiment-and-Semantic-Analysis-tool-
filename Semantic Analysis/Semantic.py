import csv

inputfile = open(r"C:\Users\pavan\OneDrive\Documents\datanewsss.csv", 'r', encoding="utf-8-sig")
csv_reader = csv.DictReader(inputfile)
linecount = 0
for line in csv_reader:
    #print(line)
    linecount = linecount + 1
    outputfile = open(r'Semenatic' + str(linecount) + '.txt', 'w')
    # csv_writer = csv.writer(outputfile)
    # data = ["Title", "Description", "Content"]
    # csv_writer.writerow(data)
    data = []
    # print(line.keys())
    data.append(line["Title"])
    data.append(line["Description"])
    data.append(line["Content"])
    data1 = ' '.join(data)
    outputfile.write(data1)

    # csv_writer.writerow(data)

