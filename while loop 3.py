# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:34:48 2020

@author: Jamie
"""

import random
a=random.randint(1,20)
i=0
while i<5:
    x=i
    b=input('you have tried '+str(x)+' times. guess a number from 1-20:')
    if int(b)==a:
        print('right')
        break
    else:
        print('try again') 
    i=i+1    
if i==5:
    print('you fail')
    
