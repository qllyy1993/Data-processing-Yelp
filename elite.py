#coding: utf-8
import csv
import re
def myreader(csv_reader):
    while True:
        try: yield next(csv_reader)
        except csv.Error:
            pass
        continue
        

with open ('/Users/LYY/Desktop/elite2import.csv','wb')as w:
    with open('/Users/LYY/Desktop/yelp_academic_dataset_user.csv','rb')as r:
        reader= myreader(csv.reader(r,delimiter=','))
        writer= csv.writer(w)
        for row in reader:
            if len(row[14])>3:
                check= re.match(r'\[[0-9]',row[14])
                if check:
                    elite= re.compile(r'([0-9]+)')
                    item= re.findall(elite,row[14])
                    for i in range(len(item)):
                        list1= [row[16],item[i]]
                        writer.writerow(list1)
