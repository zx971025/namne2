#!/use/bin/env python
# _*_coding:utf_8 _*_
import pandas as pd
import xlsxwriter
def read_schoolinformation(excel_name):
    pd.set_option('display.max_columns', None)  #显示所有列
    pd.set_option('display.max_rows', None)     #显示所有行
    df=pd.read_excel(excel_name,usecols = [2,3,7,11])
    return df
def student_no_pay(df):
    information=df.loc[df['Total Paid'].isin(['0'])]     #用于判断缴费为0,isin函数是传递为一个列表
    print(information)
    filename = '没有缴费的学生信息..xlsx'
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    information.to_excel(excel_writer=writer)                   #写入Excel
    writer.save()
def student_school(df):
    school_people=df['School'].value_counts()
    print(school_people,end='\t')
    filename1='统计各个学校的人数..xlsx'
    writer1= pd.ExcelWriter(filename1, engine='xlsxwriter')
    school_people.to_excel(excel_writer=writer1)
    writer1.save()
if __name__ == '__main__':
    excel_name= 'DSConference.xlsx'
    df=read_schoolinformation(excel_name)
    student_no_pay(df)
    student_school(df)