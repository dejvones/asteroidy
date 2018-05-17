#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:49:17 2018

@author: vla35123
"""

from math import sin, cos, radians, pi
from random import randint

import pyglet
window = pyglet.window.Window()     #Okno aplikace
batch = pyglet.graphics.Batch()     #Věcička pro efektivní vykreslování
seznam = list()

class Lod(object):
    def __init__(self, obrazek, x=None, y=None, r=None, rychlost=10,
                 window=window, batch=batch,):
        self.image = pyglet.image.load(obrazek)
        self.image.anchor_x = self.image.width//2
        self.image.anchor_y = self.image.height//2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)  
        if x:
            self._x = self.sprite.x = x
        else:
            self._x = randint(0, window.width)
        self.sprite.x = self._x
        if y:
            self._y = self.sprite.y = y
        else:
            self._y = randint(0, window.height)
        self.sprite.y = self._y
        if r:
            self._rotation = r
        else:
            self._rotation = randint(0, 360)
        self.sprite.rotation = self._rotation
        
        self._rychlost = rychlost
        seznam.append(self)

    def tiktak(self, t):
        self.sprite.x = self.sprite.x + \
            self._rychlost*t*sin((pi*self._rotation)/180)
        self._x = self.sprite.x
        self.sprite.y = self.sprite.y + \
            self._rychlost*t*cos((pi*self._rotation)/180)
        self._y = self.sprite.y

@window.event
def on_draw():
    window.clear()
    batch.draw()        #Zavolej věcičku pro efektivní vykreslování

trpaslik = Lod('obrazek.png', rychlost = 40)
enterprise = Lod('obrazek.png', rychlost = 50)
falcon = Lod('obrazek.png', rychlost = 35)

def tiktak(t):
    for lod in seznam:
        lod.tiktak(t)
    #trpaslik.tiktak(t)
    #enterprise.tiktak(t)
    #falcon.tiktak(t)

print('Trpaslik',trpaslik._x, trpaslik._y)
print('Enterprise',enterprise._x, enterprise._y)
print('Falcon',falcon._x, falcon._y)

pyglet.clock.schedule_interval(tiktak, 1/60)

pyglet.app.run()
