import board
import digitalio
import time
global pins

def init():
    INPUT_PINS = [board.IO5,board.IO7,board.IO6,board.IO3,board.IO4] #wasdm
    global pins
    pins = []
    for pin_name in INPUT_PINS:
        pin = digitalio.DigitalInOut(pin_name)
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.UP
        pins.append(pin)
    print("JoyStick Initialized")

def read():
    global pins
    states = [pin.value for pin in pins]
    return states
init()