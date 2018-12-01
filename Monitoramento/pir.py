import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pir_pin = 17
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(4, GPIO.OUT)         

try:
    while True:
        
        i = GPIO.input(pir_pin)

    if i == 0:                 
        print ("No intruders")
        GPIO.output(4, False)  
        time.sleep(0.1)
    elif i == 1:               
        print ("Intruder detected")
        GPIO.output(4, True)  #Turn ON LED
        time.sleep(0.1)

except KeyboardInterrupt:
    print ("quit")
    GPIO.cleanup()