import picamera
from time import sleep
import glob

camera = picamera.PiCamera()

camera.ISO = 100
camera.hflip = True
camera.vflip = True
camera.framerate = 50
camera.shutter_speed = 1000
camera.awb_mode ='auto'
camera.meter_mode = 'average'

i = 1

DIR = 'photo/'

while i < 2:
#    camera.start_preview()
    existing_files = glob.glob(DIR + '*.jpg')
    filename = DIR + 'image_%d.jpg' %(len(existing_files) + 1)
    print filename
    camera.capture(filename, resize = (640,480))
    i += 1
    
#camera.stop_preview()
