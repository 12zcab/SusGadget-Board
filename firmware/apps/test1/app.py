import oled
import joystick
import time

def _end_():
    oled.clear()
    oled.text("Bye Bye", 0, 0)
    time.sleep(1)
    oled.clear()
oled.clear()
oled.text("Hello World!", 0, 0)
oled.text("Hold to Exit", 0, 16)
img_path = f"{__path__}/happy.bin"
oled.draw_bin_file(img_path, 32, 32, 96, 0)

tmp = 0
while tmp <= 1:
    if joystick.read()[4] == False:
        tmp += 1
    else:
        tmp -= 1
    time.sleep(0.1)
_end_