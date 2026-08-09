import board
import digitalio
import neopixel_write
import time

global pixel_pin
def init():
    global pixel_pin
    pixel_pin = digitalio.DigitalInOut(board.IO48)
    pixel_pin.direction = digitalio.Direction.OUTPUT
    print("RGB Initialized")
def write(r,g,b):
    color_data = bytearray([g, r, b])
    global pixel_pin
    neopixel_write.neopixel_write(pixel_pin, color_data)
    
init()