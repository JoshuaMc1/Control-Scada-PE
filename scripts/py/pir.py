#!/usr/bin/python3
import subprocess
import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_PIR = 4
GPIO.setup(GPIO_PIR,GPIO.IN)

num=0
status0 = 0
status1 = 0

try :
    while True:
        status0 = 0
        print("Listo para comenzar!")
        
        while True:
            status0 = GPIO.input(GPIO_PIR)
            
            if status0==1 and status1==0:
                num=num+1
                print("Atencion se ha detectado movimiento ",num,"")
                status1=1
                time.sleep(2)
                subprocess.call("/./home/sps/examen/scripts/sh/Bzzon.sh")
                subprocess.call("/./home/sps/examen/scripts/sh/on.sh")
                time.sleep(1)
                subprocess.call("/./home/sps/examen/scripts/sh/Bzzoff.sh")
                subprocess.call("/./home/sps/examen/scripts/sh/off.sh")

            elif status0==0 and status1==1:
                print("Listo para comenzar!")
                status1=0
                time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()