#!/usr/bin/env python

import re
import time
import argparse
import RPi.GPIO as GPIO
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT, SEG7_FONT
from PIL import ImageFont


# Create matrix device
serial = spi(port=0, device=0, gpio=noop())

# Set up device based on hardware configuration
# Some setups will require rotation and block_orientation set to different values as well as the width and height
device = max7219(serial,width=32,height=48,rotate=3, block_orientation=-90,blocks_arranged_in_reverse_order=False)

print("Created device")
GPIO.setmode(GPIO.BCM)
print("Starting up")

# Shows hello message at startup to show the display is working and the Pi has successfully booted and the script is running
show_message(device, "Hello!", fill="white", font=proportional(SINCLAIR_FONT))

# Sets a custom font as a variable
fontVar = "/home/pi/max7219/pixelmix.ttf"

# Set panel brightness
brightness = 2
print("Brightness is",brightness)
device.contrast(brightness)

# All of these functions are to draw faces on the screen
# PIL is used to use a custom font, which I found took up less screen space
# compared to built in ones, as well as being more readable when shrunken down
# Get creative and make your own faces!
def drawUwU():
    with canvas(device) as draw:
        draw.text((0, 4), "UwU", font=ImageFont.truetype(fontVar,23),fill="white")

def drawCat():
    with canvas(device) as draw:
        draw.text((1, 10), "=^°w°^=", font=ImageFont.truetype(fontVar,10) ,fill="white")

def drawSmile():
    with canvas(device) as draw:
        draw.text((14, -4), ":)", font=ImageFont.truetype(fontVar,35) ,fill="white")

def drawWink():
    with canvas(device) as draw:
        draw.text((10, -4), ";)", font=ImageFont.truetype(fontVar,35) ,fill="white")

def drawCry():
    with canvas(device) as draw:
        draw.text((0, 0), "qwq", font=ImageFont.truetype(fontVar,23) ,fill="white")

def drawSmug():
    with canvas(device) as draw:
        draw.text((7, -4), "'", font=ImageFont.truetype(fontVar,35) ,fill="white")
        draw.text((10, -4), ",", font=ImageFont.truetype(fontVar,35) ,fill="white")
        draw.text((21, -4), ":)", font=ImageFont.truetype(fontVar,35) ,fill="white")

def drawAnnoyed():
    with canvas(device) as draw:
        draw.text((1, 1), ">_>", font=ImageFont.truetype(fontVar,27) ,fill="white")

def drawHappy():
    with canvas(device) as draw:
        draw.text((1, 1), "^_^", font=ImageFont.truetype(fontVar,23) ,fill="white")

def drawAngry():
    with canvas(device) as draw:
        draw.text((-4, -4), ">:(", font=ImageFont.truetype(fontVar,35) ,fill="white")

loopDraw = lambda: drawUwU()

# Set up variables used to detect short presses vs long presses
timer = 0
pressed = 0

# Set up Pi GPIO buttons - these will have to be changed according to which pins you use
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Main loop to listen for button presses
# Long presses are used to maximize the number of faces I can
# use without adding in more buttons
while True:
    if GPIO.input(17) == False:
        if pressed == 17:
            print('GPIO 17 LONG Pressed')
            loopDraw = lambda: drawCry()
        else:
            print('GPIO 17 Pressed')
            loopDraw = lambda: drawCat()
        time.sleep(0.2)
        timer = 0
        pressed = 17

    if GPIO.input(18) == False:
        if pressed == 18:
            print('GPIO 18 LONG Pressed')
            loopDraw = lambda: drawAnnoyed()
        else:
            print('GPIO 18 Pressed')
            loopDraw = lambda: drawSmug()
        time.sleep(0.2)
        timer = 0
        pressed = 18

    if GPIO.input(24) == False:
        if pressed == 24:
            print('GPIO 24 LONG Pressed')
            loopDraw = lambda: drawHappy()
        else:
            print('GPIO 24 Pressed')
            loopDraw = lambda: drawUwU()
        time.sleep(0.2)
        timer = 0
        pressed = 24

    if GPIO.input(26) == False:
        if pressed == 26:
            print('GPIO 26 LONG Pressed')
            loopDraw = lambda: drawAngry()
        else:
            print('GPIO 26 Pressed')
            loopDraw = lambda: drawSmile()
        time.sleep(0.2)
        timer = 0
        pressed = 26

    timer += 1
    loopDraw()
    time.sleep(0.2)

    if timer >= 5:
        pressed = 0
