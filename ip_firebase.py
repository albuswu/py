from urllib import urlopen
import re
from time import sleep
import smtplib
from firebase import firebase

firebase = firebase.FirebaseApplication('https://capstoneip.firebaseio.com', None)

#use checkip API to get IP address

def getPublicIP():
    data = str(urlopen('http://checkip.dyndns.com/').read())    
    IP = re.compile(r"Address: (\d+\.\d+\.\d+\.\d+)").search(data).group(1)
    return IP

#function: 1. check current ip every minute
#2. Update IP address in firebase at start
#3. monitor the ip address every minute, update in firebase if changed

current_IP = getPublicIP()

IP_name = firebase.post('/Raspberry Pi', current_IP)['name']

sleep(60)

while True:

    current_IP = getPublicIP()
    
    last_ip = firebase.get('/Raspberry Pi', None)[IP_name]

#    print last_ip
    
    if last_ip != current_IP:
        IP_name = firebase.post('/Raspberry Pi', current_IP)['name']
#        print IP_name
        sleep(60)
        
    else:
        sleep(60)
