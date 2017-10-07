#!/usr/bin/env python

import time
import RPi.GPIO as gpio
import automationhat
import os

usleep = lambda x: time.sleep(x/1000000.0)

# switch on the AH power
if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
# open-collector outputs, hence on = GND to servo
automationhat.output.one.on()

openhatch = './servo 1300 5'
closehatch = './servo 1600 5'

os.system(openhatch)
time.sleep(2)
os.system(closehatch)
time.sleep(2)

"""
# use BCM for RPi.GPIO, AH out1
pin = 5
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)
gpio.output(pin, 1)

for i in range(0,5):
    # send 1ms pulses at 50Hz
    pulse = 1600
    #automationhat.output.one.off()
    gpio.output(pin, 0)
    usleep(pulse)
    #automationhat.output.one.on()
    gpio.output(pin, 1)
    usleep(20000-pulse)

while 1:
    time.sleep(1);
"""
