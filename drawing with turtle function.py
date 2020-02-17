# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:20:16 2020

@author: Jamie
"""

import turtle
import time
t=turtle.Turtle()
t.shape('turtle')
t.color('green')
i=0
while i<720:
    time.sleep(0)
    t.forward(.5)
    t.left(.5)
    i+=1
turtle.done()    