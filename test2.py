import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
# set up GPIO output channel (LED)
led1 = 22

GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, GPIO.HIGH)


while True:
    GPIO.output(led1, GPIO.HIGH)