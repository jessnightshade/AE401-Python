# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:14:27 2020

@author: Jamie
"""

num=input('number of students:')
scorelist=[]
namelist=[]
high=0
low=100
highname=''
lowname=''
for i in range (int(num)):
    students_name=input('student:')
    score=input('score:')
    scorelist.append(int(score))
    namelist.append(students_name)
    if int(score)>high:
        high=int(score)
        highname=students_name
    if int(score)<low:
        low=int(score)
        lowname=students_name
Avg=sum(scorelist)/int(num)
print('highest score:',high)
print('lowest score:',low)
print('average:',Avg)   