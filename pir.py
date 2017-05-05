import time 

import RPi.GPIO as io 
io.setmode(io.BCM)
import glob

pir_pin_in = 18
pir_pin_out = 23

io.setup(pir_pin_out, io.IN) # activate input
io.setup(pir_pin_in, io.IN) # activate input


while True:

    while io.input(pir_pin_out):
        print "Car going out!"
        time.sleep(0.33)
        if io.input(pir_pin_out)==0:
            print "Ended!"

    while io.input(pir_pin_in):
        print "Car going in!"
        time.sleep(0.33)
        if io.input(pir_pin_in)==0:
            print "Ended!"            
            
        
