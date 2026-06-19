# SusGadget
Welp this usb is kinda sus u know
Try to plug it onto your computer or power it
may be it will hijack ur computer with HID magic power
or may be it will connect Bluetooth to ur phone and play rickroll?
or it... may even send weird signals to aliens! :|

# Zine
![Zine](https://github.com/12zcab/SusGadget-Board/blob/main/Zine.png)

# Images
![Design](https://github.com/12zcab/SusGadget-Board/blob/main/img/design.png)
![Routing](https://github.com/12zcab/SusGadget-Board/blob/main/img/routing.png)
![PCBF](https://github.com/12zcab/SusGadget-Board/blob/main/img/pcbf.png)
![PCBB](https://github.com/12zcab/SusGadget-Board/blob/main/img/pcbb.png)

# Assembled Images
![3Ddesign](https://github.com/12zcab/SusGadget-Board/blob/main/img/3Ddesign.png)
![3DF](https://github.com/12zcab/SusGadget-Board/blob/main/img/3DF.png)
![3DB](https://github.com/12zcab/SusGadget-Board/blob/main/img/3DB.png)

# How to Assemble
1.Solder all the SMD components (CH340C,Joystick,USBA)

2.Solder 2.54 Socket and PinHeaders

3.Solder the 104 Capacitor

4.Solder the Buzzer (or a mini Speaker if u want)

5.Test and Solder the ESP32 S3 Supermini

6.Solder the Potentiometer

# What is this
Yah this sus usb stick gadget is a esp32 S3 supermini based (depends on your preferred function and cost) board with i2c port, a usb Power and UART port with onboard ch340c and a mini joystick !
it also have a potentiometer and a buzzer so may be u can make some weird beep noise that changes its pitch while u spin the potentiometer and communicate with aliens (welp, who knows?)
Definitely a cool gadget and definitely sus enough :D

# Why I made this :|
Humm idk this is like what people think electronic nerds will make : |
(Actually i wanna try to plug in this usb and tell my friend this is just a oled small screen to monitor his computer's temperature then shutdown his computer with Alt+F4+Enter while he plays Roblox :DDDDD)

# What it can do?
 1.A 0.91 inch Oled for Display
 
 2.A Potentiometer for Analog Input
 
 3.A Joystick Module Connecter
 
 4.A RGB WS2812 LED on board
 
 5.A USB-A with CH340 on board serial interface (and for power)
 
 6.Extend IO Ports (GPIO,I2C)
 
 7.5-Way Joy-Stick like Switch
 
 8.a buzzer :D

# How to Assemble it
 1.Solder all SMD components first
 
 2.Test and burn firmware to the ESP32 S3 Supermini
 
 3.Solder All the 2.54 PinHeaders and PinSockets
 
 4.Solder Other Components
 
 5.Enjoy using this for hacking ur friend's computer :D

# Logs 15/6/2026
https://item.taobao.com/item.htm?abbucket=20&id=950239319026&mi_id=0000WqR8OMQpzP-0tstqVlaIIE-5s_AjfzWIlYg7Y13UQbU&ns=1&priceTId=2100c8cd17815317343675137e0713&skuId=6028621276205&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%2277800c1798fd66c0a4317fe7f9f78c3a%22%7D&xxc=taobaoSearch
SDA=GPIO1，SCL=GPIO0，地址=0x3C
https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.100b2e8d51NHLx&id=739043147728&mi_id=0000kuWiKHqk9L-WG5OeO-tR0Vil6JLB2OPHXTrULPq59wQ
https://detail.tmall.com/item.htm?abbucket=20&id=794614101743&mi_id=0000qOcdzZeWCjtFCki57O45Viz5gVgWm_UBMkDzrkOda24&ns=1&priceTId=2100c91317815328317171037e073a&skuId=5425005817400&spm=a21n57.1.hoverItem.12&utparam=%7B%22aplus_abtest%22%3A%22b916618d60f8ef9a19f1674b827a0030%22%7D&xxc=taobaoSearch
what it need to have:
1.i2c extend pin
2.a ESP32 C3 with oled screen
3.USB A serial
4.a mini joystick module (05x2.54)
5.a 6mm button for programming use
6.a Rotary Knob
7.Buzzer
what i did today:
1.finished designing and routing the main board
2.Write part of the readme.md
Todo List:
1.Render the better Quality Product with Fusion
2.finish the readme.md
3.design the zine
4.write a simple firmware

btw i found some problem... that board is not fully capable with the supermini....
i gotta redesign it later i think

# Logs 16/6/2026
Decided to use normal supermini and add a oled screen myself :|

https://detail.tmall.com/item.htm?abbucket=20&id=611352518150&mi_id=0000pYwxGRzYKRLn4FzhkfKE19J5gkulzfIQ9u5VuWXrN1U&ns=1&priceTId=2100cff617815993482653591e0737&spm=a21n57.1.hoverItem.7&utparam=%7B%22aplus_abtest%22%3A%224c6de8d9686da9c172b3bdc47aa9a279%22%7D&xxc=taobaoSearch

what i did today:
1.Redesigned the board
2.Routed the board again
3.choose better components
4.Wrote some Readme.md
5.Finished the Zine
6.Welp Basically Finished EVERYTHING OMG
