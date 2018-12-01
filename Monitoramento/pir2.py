import RPi.GPIO as GPIO
import time
from time import gmtime, strftime

GPIO.setmode(GPIO.BCM)
pinopir = 17
GPIO.setup(pinopir, GPIO.IN)
GPIO.setup(4, GPIO.OUT)

try:
    while True:
        if GPIO.input(pinopir):
            GPIO.output(4, True)
            time.sleep(1)
            timex = strftime ("%d-%m-%Y %H:%M:%S", gmtime())
            print (timex +  " MOVIMENTO DETECTADO")
            time.sleep(1)
            GPIO.output(4, False)
        time.sleep(1)
except KeyboardInterrupt:
    print ("quit")
    GPIO.cleanup()