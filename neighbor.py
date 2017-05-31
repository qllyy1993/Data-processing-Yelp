#coding: utf-8
import csv
import re
def myreader(csv_reader):
    while True:
        try: yield next(csv_reader)
        except csv.Error:
            pass
        continue
        

with open ('/Users/LYY/Desktop/neighborhoods2import.csv','wb')as w:
    with open('/Users/LYY/Desktop/neighbor.csv','rb')as r:
        reader= myreader(csv.reader(r,delimiter=','))
        writer= csv.writer(w)
        for row in reader:
            if len(row[1])>3:
                check= re.match(r'\[\'.+\'',row[1])
                if check:
                    neighborhoods= re.compile(r'(\'[A-Za-z\s]+\')')
                    item= re.findall(neighborhoods,row[1])
                    for i in range(len(item)):
                        list1= [row[0],item[i]]
                        writer.writerow(list1)
