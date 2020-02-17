# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:11:19 2020

@author: Jamie
"""

import turtle
import time
t=turtle.Turtle()
t.shape('turtle')
t.color('green')
for i in range(720):
    time.sleep(0)
    t.forward(.5)
    t.left(.5)
turtle.done()    