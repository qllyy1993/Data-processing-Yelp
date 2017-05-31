#coding: utf-8
import csv
import re
def myreader(csv_reader):
    while True:
        try: yield next(csv_reader)
        except csv.Error:
            pass
        continue
        

with open ('/Users/LYY/Desktop/friends.csv','wb')as w:
    with open('/Users/LYY/Desktop/yelp_academic_dataset_user.csv','rb')as r:
        reader= myreader(csv.reader(r,delimiter=','))
        writer= csv.writer(w)
        for row in reader:
            if len(row[3])>3:
                check= re.match(r'\[\'.+\'',row[3])
                if check:
                    friends= re.compile(r'(\'[A-Za-z0-9\-]+\')')
                    item= re.findall(friends,row[3])
                    for i in range(len(item)):
                        list1= [row[16],item[i]]
                        writer.writerow(list1)
