import time 
import RPi.GPIO as io 
io.setmode(io.BCM)
import picamera
import glob
from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi() # assumes environment variables are set.
 
pir_pin = 18

io.setup(pir_pin, io.IN) # activate input

category = ['people','woman','man','girl','boy']
length_category = len(category)

camera = picamera.PiCamera()

#camera.ISO = 400
camera.hflip = True
camera.vflip = True
#camera.framerate = 0.01
#camera.shutter_speed = 10000000
camera.awb_mode ='auto'
camera.meter_mode = 'average'

DIR = '../test_images/'

while True:
    if io.input(pir_pin):
        print "Motion Detected!"
        print "Taking Picture!"

        existing_files = glob.glob(DIR + '*.jpg')
        filename = DIR + 'image_%d.jpg' %(len(existing_files) + 1)
        camera.capture(filename, resize = (800,600))
        print "Picture Obtained!"
	print "Analyzing!"	

        result = clarifai_api.tag_images(open(filename, 'rb'))

#	print "results:"	

        length_results = len(result['results'][0]['result']['tag']['classes'])

        for i in range(length_results):
            tag = result['results'][0]['result']['tag']['classes'][i]
#            print result['results'][0]['result']['tag']['classes'][i]
            for j in range(length_category):
#                print category[j]
                if tag == category[j]:
                    print "Human Detected!"
                    j = length_category + 1 
                    i = length_results + 1
                
	time.sleep(5);
