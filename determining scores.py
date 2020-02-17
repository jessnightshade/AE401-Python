# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:46:06 2020

@author: Jamie
"""

num=input('number of students:')
scorelist=[]
namelist=[]
high=0
low=0
#highname=''
#lowname=''
for i in range (int(num)):
    students_name=input('student:')
    score=input('score:')
    scorelist.append(int(score))
    namelist.append(students_name)
    if int(score)>scorelist[high]:
        high=i
        #highname=students_name
    if int(score)<scorelist[low]:
        low=i
        #lowname=students_name
Avg=sum(scorelist)/int(num)
for j in range (int(num)):
    if scorelist[j]==scorelist[high]:
        print('highest score:',scorelist[j],namelist[j])
for k in range (int(num)):
    if scorelist[k]==scorelist[low]:
        print('lowest score:',scorelist[k],namelist[k])
print('average:',Avg)       
    
    
    