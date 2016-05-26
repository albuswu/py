import picamera
from time import sleep
import glob

camera = picamera.PiCamera()

camera.ISO = 800
camera.hflip = True
camera.vflip = True
#camera.framerate = 30
camera.shutter_speed = 30000
camera.awb_mode ='auto'
#camera.meter_mode = 'average'

i = 1

DIR = 'photo/'

while i < 2:
#    camera.start_preview()
    existing_files = glob.glob(DIR + '*.jpg')
    filename = DIR + 'image_%d.jpg' %(len(existing_files) + 1)
    print filename
    camera.capture(filename, resize = (1024,768))
    i += 1
    sleep(5)
    
#camera.stop_preview()
