import RPi.GPIO as GPIO

import time
import os


STEP = 2
DELAY = 0.5

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel (LED)
led1 = 18

#GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led1,GPIO.OUT, pull_up_down=GPIO.PUD_UP)



# blinking function
def blink(pin):
       GPIO.output(pin,GPIO.LOW)
       time.sleep(DELAY)
       GPIO.output(pin,GPIO.HIGH)
       time.sleep(DELAY)
       return
 
def pwm(pin, angle):
    print "servo[" + str(pin) + "][" + str(angle) + "]"
    cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/servoblaster"
    os.system(cmd)
    #time.sleep(DELAY)
 
while True: 
        for j in range(0, 249, STEP):
            pwm(2,j)
        time.sleep(DELAY)
        for j in range(249, 0, (STEP*-1)):
            pwm(2,j)
        time.sleep(DELAY)
        GPIO.output(led1, GPIO.LOW)
        time.sleep(2)