import time
import board
import pwmio
global buzzer
def init():
    global buzzer
    buzzer = pwmio.PWMOut(board.IO8, frequency=1000, duty_cycle=0, variable_frequency=True)
    print("Buzzer Initialized")
def play_tone(frequency, duration):
    global buzzer
    buzzer.frequency = frequency
    buzzer.duty_cycle = 32768
    time.sleep(duration)
    buzzer.duty_cycle = 0
def active():
    global buzzer
    buzzer.duty_cycle = 32768
def deactive():
    global buzzer
    buzzer.duty_cycle = 0
def freq(fre):
    global buzzer
    buzzer.frequency = fre
def play_series(frequencies, durations):
    for frequency,duration in zip(frequencies, durations):
        if frequency == 0:
            time.sleep(duration)
        else:
            play_tone(frequency,duration)
init()

#play_series([659, 622, 659, 622, 659, 494, 587, 523, 440, 0, 262, 330, 440, 494, 0, 330, 494, 523, 659], [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.2, 0.3, 0.3, 0.3, 0.6, 0.2, 0.3, 0.3, 0.3, 0.6])
#hehe an easter egg
# 12zcab 4/Aug/2026 01:17a.m.