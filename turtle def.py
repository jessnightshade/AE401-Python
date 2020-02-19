# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:20:27 2020

@author: Jamie
"""

import turtle
t=turtle.Turtle()

def drawsquare(unit):
    for i in range(4):
        t.forward(unit)
        t.left(90)

drawsquare(100)
turtle.done()