#! /usr/bin/python

import RPi.GPIO as GPIO
import sys, os, time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #camera output pin

image_num = 1

GPIO.output(3, False)

while True:
    if GPIO.input(11):                 #When output from motion sensor is LOW
	# Also need to look into python picamera module
        os.system("raspistill -o test_images/test.jpg")
        GPIO.output(3, True)
	os.system("time ./bash_scripts/run_sample.sh test_images/test.jpg")
        time.sleep(4)
        GPIO.output(3, False)

            




