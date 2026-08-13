import buzzer
import potentiometer
import joystick
import oled
import math

oled.clear()
Heartz = 440

currentInterval = 4

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

while True:
    oled.clear_noupdate()
    joy_in = joystick.read()
    if joy_in[0] == False:
        currentInterval = 3
    elif joy_in[1] == False:
        currentInterval = 5
    elif joy_in[2] == False:
        currentInterval = 4
    elif joy_in[3] == False:
        currentInterval = 6
    pot_val = potentiometer.read()
    currentNote_Offset = min(int(pot_val / 85.42), 11)
    note_name = NOTE_NAMES[currentNote_Offset] + str(currentInterval)
    midi_note = (currentInterval + 1) * 12 + currentNote_Offset
    Heartz = int(440 * math.pow(2, (midi_note - 69) / 12))
    display_text = f"{note_name} ({Heartz}Hz)"
    oled.text(display_text, 10, 10)
    buzzer.freq(Heartz)
    if joy_in[4] == False:
        buzzer.active()
    else:
        buzzer.deactive()
