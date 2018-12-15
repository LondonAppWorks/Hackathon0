import RPi.GPIO as GPIO
import time
import os

hostname = raw_input("Add host: ")
response = os.system("ping -c 1 " + hostname)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

if response == 0:
    GPIO.output(18,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(18,GPIO.LOW)
else:
    GPIO.output(23,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(23,GPIO.LOW)
