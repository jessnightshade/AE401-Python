# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:56:26 2020

@author: Jamie
"""

scorelist=[]
num=input('how many scores:')
for i in range(int(num)):
    scores=input('score:')
    scorelist.append(int(scores))
print(max(scorelist))    
print(min(scorelist))    
print(len(scorelist))    
print(sum(scorelist))    
print(sorted(scorelist))
