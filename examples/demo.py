#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import argparse
import RPi.GPIO as GPIO
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT, SEG7_FONT
from PIL import ImageFont
from luma.core.virtual import viewport


# create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial,width=32,height=48,rotate=3, block_orientation=-90,blocks_arranged_in_reverse_order=False)
print("Created device")
GPIO.setmode(GPIO.BCM)
# start demo
#msg = "Hello world"
#print(msg)
virtual = viewport(device, width=200, height=100)

def drawUwU():
    with canvas(device) as draw:
        draw.text((0, 4), "UwU", font=ImageFont.truetype("pixelmix.ttf",23),fill="white")

def drawCat():
    with canvas(device) as draw:
        draw.text((1, 10), "=^°w°^=", font=ImageFont.truetype("pixelmix.ttf",10) ,fill="white")

def drawSmile(sleepTime):
    with canvas(device) as draw:
        draw.text((14, -4), ":)", font=ImageFont.truetype("pixelmix.ttf",35) ,fill="white")
    time.sleep(sleepTime)

def drawWink(sleepTime):
    with canvas(device) as draw:
        draw.text((10, -4), ";)", font=ImageFont.truetype("pixelmix.ttf",35) ,fill="white")
    time.sleep(sleepTime)

def drawCry(sleepTime):
    with canvas(device) as draw:
        draw.text((0, 0), "qwq", font=ImageFont.truetype("pixelmix.ttf",23) ,fill="white")
    time.sleep(sleepTime)

def drawSmug(sleepTime):
    with canvas(device) as draw:
        draw.text((7, -4), "'", font=ImageFont.truetype("pixelmix.ttf",35) ,fill="white")
        draw.text((10, -4), ",", font=ImageFont.truetype("pixelmix.ttf",35) ,fill="white")
        draw.text((20, -4), ":)", font=ImageFont.truetype("pixelmix.ttf",35) ,fill="white")
    time.sleep(sleepTime)

def drawAnnoyed():
    with canvas(device) as draw:
        draw.text((1, 1), ">_>", font=ImageFont.truetype("pixelmix.ttf",27) ,fill="white")

def drawImageVirtual():
    with canvas(virtual) as draw:
        #draw.rectangle(device.bounding_box,outline='white')
        text(draw,(5,5),"UWU",fill="white",font=SEG7_FONT)
        #text(draw,(0,9),"World",fill="white",font=proportional(LCD_FONT))
        draw.rectangle(device.bounding_box, outline="white", fill="black")
    for offset in range(8):
        virtual.set_position((offset, offset))
        time.sleep(0.1)

def drawTiny(textToDraw):
    with canvas(device) as draw:
#        draw.rectangle(device.bounding_box,outline='white',fill="white")
#        draw.rectangle(((1,1),(3,3)),outline='white',fill="white")
#        text(draw,(5,5),"UWU",fill="black",font=CP437_FONT)
        draw.text((0, 0), textToDraw, font=TINY_FONT,fill="white")
    time.sleep(60)

loopDraw = lambda: drawUwU()

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(17) == False:
        print('GPIO 17 Cat Pressed')
        loopDraw = lambda: drawCat()
        time.sleep(0.2)
    if GPIO.input(18) == False:
        print('GPIO 18 Annoyed Pressed')
        loopDraw = lambda: drawAnnoyed()
        time.sleep(0.2)
    loopDraw()

