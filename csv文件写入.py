#!/use/bin/env python
# _*_coding:utf_8 _*_
import csv
import json
csvFile= open("DSConference.csv", "r")
csv_files=csv.DictReader(csvFile)
collection_list=[]
for csv_file in csv_files:
    collection_list.append(csv_file)
print('以下为没有缴费的学生信息')
informations=[]
for i in range(len(collection_list)):
    if collection_list[i]['Total Paid']=='0':
        information='First Name:{},Last Name:{},School:{},'.format(collection_list[i]['First Name'],collection_list[i]['Last Name'],collection_list[i]['School'])
        informations.append(information)
        print(information)
print('以下为统计各学校的人数')
index=0
schools=[]
for i in range(len(collection_list)):
    schools.append(collection_list[i]['School'])
index=0
number={}
for school in schools:
    if school in number:
        number[school]+=1
    else:
        number[school]=1
print(number)
with open('2.json','w')as f:
    f.write(json.dumps(number))
with open('3.text', 'w',newline='\n')as f:
    f.writelines(informations)
