import time 
import RPi.GPIO as io 
io.setmode(io.BCM)
import picamera
import glob
from clarifai.client import ClarifaiApi
import subprocess, sys

clarifai_api = ClarifaiApi() ## assumes environment variables are set.
 
pir_pin_out = 23
pir_pin_in = 18

## activate input
io.setup(pir_pin_out, io.IN)
io.setup(pir_pin_in, io.IN) 

category = ['car','auto','cars','vehicle']

DIR = '../test_images/'

length_category = len(category)
camera = picamera.PiCamera()

##define camera specs
camera.ISO = 400
camera.hflip = True
camera.vflip = True
camera.framerate = 50
camera.shutter_speed = 5000
camera.awb_mode ='auto'
camera.meter_mode = 'average'

##-------------------------------------------------------------------
##define a function to take a photo and upload to clarifai to analyze, return tags
def taking_photo():
    print "Motion Detected!"
    print "Taking Picture!"

    existing_files = glob.glob(DIR + '*.jpg')
    filename = DIR + 'image_%d.jpg' %(len(existing_files) + 1)
    camera.capture(filename, resize = (640,480))
    print "Picture Obtained!"
    print "Analyzing!"	

    result = clarifai_api.tag_images(open(filename, 'rb'))
    return result
    print "done processing results from clarifai"
    print "results:"	

##define a function to analyze the tags to see if a car's detected
def analyze(result):
    length_results = len(result['results'][0]['result']['tag']['classes'])    
    for i in range(length_results):
        tag = result['results'][0]['result']['tag']['classes'][i]
        for j in range(length_category):
            if tag == category[j]:
                print "Car Detected!"
                print "Triggering Photon!"
                return 1
                break

##-------------------------------------------------------------------
##main function
while True:
    ##if the inner motion sensor detects motion first
    if io.input(pir_pin_out):
        result = taking_photo()
        value = 0
        value = analyze(result)
        print "going out!"
        if value:
            print "Car going out!"
            subprocess.Popen([sys.executable,"photon_trigger_out.py"])
            while io.input(pir_pin_out):
                time.sleep(1)            
        if io.input(pir_pin_out) == 0:
            print "ended"

    ##if the outer motion sensor detects motion first		
    if io.input(pir_pin_in):
        result = taking_photo()
        value = 0
        value = analyze(result)
        print "going in!"
        if value:
            print "Car going in!"
            subprocess.Popen([sys.executable,"photon_trigger_in.py"])
            while io.input(pir_pin_in):
                time.sleep(1)            
        if io.input(pir_pin_in) == 0:
            print "ended"

