#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
python 起始ip和ip总数列出每个ip

'''


import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
data = xlrd.open_workbook('X:\ip.xlsx')
filewrite = open("D:\eachip.txt", 'a')
table = data.sheets()[0]
nrows = table.nrows
countlist = []
iplist = []
for x in range(nrows-1):
    countlist.append(int(table.cell(x+1, 2).value))
for y in range(nrows-1):
    iplist.append(table.cell(y + 1, 1).value)
for i in range(len(countlist)):
    ip = iplist[i]
    count = countlist[i]
    ss = ip.split('.')
    num1 = int(ss[0])
    num2 = int(ss[1])
    num3 = int(ss[2])
    num4 = int(ss[3])

    for i in range(count):

        if num4 > 254:

            num3 +=1
            num4 = 1
            if num3 > 254:

                num2 += 1
                num3 = 1
                num4 = 1


                if num2 > 254:

                    num1 += 1
                    num2 = 1
                    num3 = 1
                    num4 = 1
        num4 += 1
        resaut = str(num1) + str('.') + str(num2) + str('.') + str(num3) + str('.') + str(num4)
        print (resaut)
        filewrite.write(resaut + '\n')

# ip = "1.34.0.0"
# count = 131072
