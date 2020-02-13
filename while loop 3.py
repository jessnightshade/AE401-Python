# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:34:48 2020

@author: Jamie
"""

import random
a=random.randint(1,20)
print('you have 5 tries')
i=1
while i<6:
    b=input('guess a number from 1-20:')
    if int(b)==a:
        print('right! you have tried '+str(i)+' times. ')
        break
    elif int(b)<a:
        print('wrong! you have tried '+str(i)+' times. try a higher number')
    elif int(b)>a:
        print('wrong! you have tried '+str(i)+' times. try a lower number number')
    i=i+1    
if i==6:
    print('you fail')
    
