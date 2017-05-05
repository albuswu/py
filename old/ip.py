from urllib import urlopen
import re
from time import sleep
import smtplib

#use checkip API to get IP address

def getPublicIP():
    data = str(urlopen('http://checkip.dyndns.com/').read())    
    IP = re.compile(r"Address: (\d+\.\d+\.\d+\.\d+)").search(data).group(1)
    return IP

#function: 1. check current ip every minute
#2. send an email of current ip at first start
#3. save ip to a file and send email if the ip changes
current_IP = getPublicIP()

while True:

    current_IP = getPublicIP()
    
    f = open('IP_address.txt','r')
    ip_last = f.readline().rstrip('\n')
    f.close()
    
    if ip_last == current_IP:
        f.close()

    else:
        f = open('IP_address.txt','r')
        iplog = f.readlines()
        f.close()
        
        f = open('IP_address.txt','w')
        f.truncate()
        iplog.insert(0,current_IP+'\n')
        iplog = "".join(iplog)
        f.write(iplog)
        f.close()
        
    sleep(5)
