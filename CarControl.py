import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import spidev
import os


# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel (Motor and Servo)
motor1 = 18
steering1 = 22

GPIO.setup(motor1,GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(motor1, GPIO.LOW)

STEP = 2
DELAY = 0.1

def FlashDesk():
    for i in range (0,2):    
        for j in range(1, 249, STEP):
            pwm(2,j)
        time.sleep(DELAY)
        for j in range(249, 1, (STEP*-1)):
            pwm(2,j)
        time.sleep(DELAY)
        os.system("echo 2=0 > /dev/servoblaster")

def pwm(pin, angle):
    print "servo[" + str(pin) + "][" + str(angle) + "]"
    cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/servoblaster"
    os.system(cmd)
    #time.sleep(DELAY)

while True:
    inputkey = raw_input()
    if inputkey == "w":
        print("Forward")
        FlashDesk()
    elif inputkey == "s":
        print("Back")
        FlashDesk()
    elif inputkey == "a":
        print("Left")
        FlashDesk()
    elif inputkey == "d":
        print("Right")
        FlashDesk()
    
    

print("<==== End of Program ====>")