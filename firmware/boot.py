import sys
import storage
import usb_cdc
import usb_hid
import usb_midi
import interface.oled
interface.oled.clear()
interface.oled.text("Sus-Gadget",0,0)
interface.oled.text("Booting.",0,16)
usb_midi.disable()
print("Disabled Midi")
interface.oled.text(".",45,16)
usb_cdc.enable(console=True, data=False)
print("Enabled CDC")
interface.oled.text(".",50,16)
usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.MOUSE))
print("Enabled HID")
interface.oled.text(".",55,16)
storage.remount("/", readonly=False)
print("Disabled Flash")
interface.oled.text(".",60,16)
m = storage.getmount("/")
m.label = "SusGadget"
print("Renamed Flash")
interface.oled.text(".",65,16)
storage.remount("/", readonly=True)
print("Enabled Flash")
interface.oled.text(".",70,16)
if "/interface" not in sys.path:
    sys.path.append("/interface")
if "/apps" not in sys.path:
    sys.path.append("/apps")
print("Added System Paths")
interface.oled.text(".",75,16)
print("[Boot] Finished")
