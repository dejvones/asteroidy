#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:26:15 2018

@author: vla35123
"""

import pyglet
from math import sin, cos, pi
from pyglet.window.key import DOWN, UP, LEFT, RIGHT

window = pyglet.window.Window()

obrazek = pyglet.image.load('obrazek.png')
obrazek.anchor_x = obrazek.width //2
obrazek.anchor_y = obrazek.height //2
sprite = pyglet.sprite.Sprite(obrazek)

uhel = 0
sprite.rotation = 0
rychlost = 20
klavesy = set()

def tiktak(t):
    global rychlost
    global uhel
    #posun
    sprite.x = sprite.x + rychlost*t*sin((pi*uhel)/180)
    sprite.y = sprite.y + rychlost*t*cos((pi*uhel)/180)
    
    #natočení

    for sym in klavesy:
        if sym == DOWN:
            if rychlost - 20 >= 0:
                rychlost -= 20
            else:
                pass
        elif sym == UP:
            if rychlost + 20 <= 100:
                rychlost += 20
            else:
                pass
        elif sym == RIGHT:
            sprite.rotation +=10
            uhel += 10
        elif sym == LEFT:
            sprite.rotation -=10
            uhel -=10


@window.event
def on_draw():
    window.clear()
    sprite.draw()


@window.event
def on_mouse_press(x, y, button, mod):
    global uhel
    if button == 1:
        sprite.x = x
        sprite.y = y
    elif button == 4:
        sprite.rotation += 10
        uhel += 10

@window.event
def on_key_press(sym, mod):
    global klavesy
    klavesy.add(sym)
    
@window.event
def on_key_release(sym, mod):
    global klavesy
    klavesy.remove(sym) 
    



pyglet.clock.schedule_interval(tiktak, 1/60)


pyglet.app.run()
print('Hotovo!')
