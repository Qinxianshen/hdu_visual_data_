#-*- coding:utf-8 -*-
import csv

csvfile = open('export.csv', 'wb')  #打开方式还可以使用file对象
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄'])

data = [
    ('qinzijing', '21'),
    ('qinziwei', '19')
]
writer.writerows(data)

csvfile.close()
