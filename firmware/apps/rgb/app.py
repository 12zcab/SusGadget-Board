import oled
import joystick
import potentiometer
import rgb as light
global select
global rgb
def map_range_int(val):
    return round((val / 255.0) * 88)
def init():
    global select
    global rgb
    select = 0
    oled.clear()
    loop()
def loop():
    global select
    global rgb
    rgb = [0,0,0]
    select_cooldown = 0
    cont = True
    while cont:
        oled.clear_noupdate()
        oled.rect_noupdate(5, 5, 90, 5, 1)
        oled.rect_noupdate(5, 15, 90, 5, 1)
        oled.rect_noupdate(5, 25, 90, 5, 1)
        oled.rect_noupdate(6, 6, map_range_int(rgb[0]), 3, 1,True)
        oled.rect_noupdate(6, 16, map_range_int(rgb[1]), 3, 1,True)
        oled.rect_noupdate(6, 26, map_range_int(rgb[2]), 3, 1,True)
        if select_cooldown == 0:
            joy_in = joystick.read()
            if joy_in[0] == False:
                select -= 1
                select_cooldown = 3
            if joy_in[1] == False:
                select += 1
                select_cooldown = 3
            if joy_in[2] == False:
                oled.clear()
                cont = False
        if select < 0:
            select = 0
        if select > 2:
            select = 2
        if select_cooldown > 0:
            select_cooldown -= 1
        oled.rect_noupdate(4, select * 10 + 4, 92, 7, 1)
        if potentiometer.read() == 1024:
            rgb[select] += 4
        elif potentiometer.read() == 0:
            rgb[select] -= 4
        rgb = [max(0, min(255, x)) for x in rgb]
        light.write(rgb[0],rgb[1],rgb[2])
        oled.show()
init()