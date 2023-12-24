# Brian Lesko
# Arduino Nano Esp 32 - Micropython
# https://docs.arduino.cc/micropython-course/course/introduction-python

# PWM - Pulse Width Modulation for controlling the speed of a brushed dc motor

import machine
import time

from machine import Pin, PWM, ADC

pwm = PWM(Pin(13))
pwm.freq(1000) # 1000 times a second

while True:
    pwm.duty_u16(65000) # _u16 increases range from 0 to 65535, by default its 0 to 1023

