import RPi.GPIO as GPIO
import random

import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in range(len(dac)):
    number.append(random.randint(0, 1))
#number = [0, 0, 0, 0, 0, 0, 0, 1]
#2
#number = [1, 1, 1, 1, 1, 1, 1, 1]
#255
#number = [0, 1, 1, 1, 1, 1, 1, 1]
#127
#number = [0, 0, 1, 1, 1, 1, 1, 1]
#64
#number = [0, 0, 0, 1, 1, 1, 1, 1]
#32
number = [0, 0, 0, 0, 1, 1, 1, 1]
#5
#number = [0, 0, 0, 0, 0, 0, 0, 0]
#0
#number = [1, 0, 0, 0, 0, 0, 0, 0]
#256

for i in range(len(dac)):
    GPIO.output(dac[i], number[i])
time.sleep(12)

for i in range(len(dac)):
    GPIO.output(dac, 0)
GPIO.cleanup()

