import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
global kbd
def init():
    global kbd
    kbd = Keyboard(usb_hid.devices)
def send(*args):
    global kbd
    kbd.send(*args)
init()