import RPi.GPIO as GPIO
import time
import wiringpi2

OUTPUT = 1

PIN_TO_PWM = 1

wiringpi2.wiringPiSetup()
wiringpi2.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi2.softPwmCreate(PIN_TO_PWM,0,100) # Setup PWM using Pin, Initial Value and Range parameters

STEP = 2
DELAY = .5


def FlashDesk():
    for i in range (0,5):    
        for j in range(0, 100, STEP):
            wiringpi2.softPwmWrite(PIN_TO_PWM,j)
            wiringpi2.delay(50)
        
        for j in range(100, 0, (STEP*-1)):
            wiringpi2.softPwmWrite(PIN_TO_PWM,j)
            wiringpi2.delay(50)
        
wiringpi2.softPwmWrite(PIN_TO_PWM,100)
while True:
    wiringpi2.softPwmWrite(PIN_TO_PWM,100)
    #FlashDesk()
    
