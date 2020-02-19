# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:54:53 2020

@author: Jamie
"""

num=input('number of students:')
name_and_score_list=[]
high=0
low=100
for i in range (int(num)):
    students_name=input('student:')
    name_and_score_list.append(students_name)
    score=input('score:')
    name_and_score_list.append(score)
    
total=0
for i in range (1,2*int(num),2):
    total=total+int(name_and_score_list[i])
    avg=total/int(num)
    if int(name_and_score_list[i])>high:
        high=int(name_and_score_list[i])
        highname=name_and_score_list[i-1]
    if int(name_and_score_list[i])<low:
        low=int(name_and_score_list[i])
        lowname=name_and_score_list[i-1]
print(name_and_score_list)
print('the class average is:',avg)        
print('the highest score is ',high)
print('the lowest score is ',low)