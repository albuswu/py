import time 
import RPi.GPIO as io 
io.setmode(io.BCM)
import sys, os, requests
import picamera
import glob
from clarifai.client import ClarifaiApi
#from urllib2 import Request, urlopen
#import unirest
#import json

clarifai_api = ClarifaiApi() # assumes environment variables are set.
 
pir_pin = 18

io.setup(pir_pin, io.IN) # activate input

category = ['car','auto','cars','vehicle','girl','boy','man','woman','human']

DIR = '../test_images/'

length_category = len(category)
camera = picamera.PiCamera()

camera.ISO = 1000
camera.hflip = True
camera.vflip = True
#camera.framerate = 0.01
camera.shutter_speed = 30000
camera.awb_mode ='auto'
camera.meter_mode = 'average'

urltrigger = 'https://api.particle.io/v1/devices/310047000447343232363230/detect-spots'
query = {'access_token':'f8093528e7b81caceeaecd0569423df524dffbab'}
urlget = 'https://api.particle.io/v1/devices/310047000447343232363230/spot1?access_token=f8093528e7b81caceeaecd0569423df524dffbab'


while True:
    if io.input(pir_pin):
        print "Motion Detected!"
        print "Taking Picture!"

        existing_files = glob.glob(DIR + '*.jpg')
        filename = DIR + 'image_%d.jpg' %(len(existing_files) + 1)
        camera.start_preview()
        camera.capture(filename, resize = (1024,768))
        camera.stop_preview()
	print "Picture Obtained!"
	print "Analyzing!"	

        result = clarifai_api.tag_images(open(filename, 'rb'))
#        print result
	print "done processing results from clarifai"
	print "results:"	

        length_results = len(result['results'][0]['result']['tag']['classes'])

        for i in range(length_results):
            tag = result['results'][0]['result']['tag']['classes'][i]
#            print result['results'][0]['result']['tag']['classes'][i]
            for j in range(length_category):
#                print category[j]
                if tag == category[j]:
                    print "Car Detected!"
                    print "Triggering Photon!"
                    res = requests.post(urltrigger, data=query)
                    photon =  requests.get(urlget)
                    print photon.text
                    print(res.text)
                    break
                
	print "ended"
	
	time.sleep(10);
	
	

