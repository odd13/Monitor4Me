import time
import spidev

import RPi.GPIO as GPIO
import time
import MySQLdb
from time import gmtime, strftime
import feedparser
import os

from espeak import espeak
from datetime import datetime


# blinking function
def blink(pin):
       GPIO.output(pin,GPIO.LOW)
       time.sleep(.1)
       GPIO.output(pin,GPIO.HIGH)
       time.sleep(.1)
       return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel (LED)
led1 = 18

GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, GPIO.HIGH)

#Flash when torrent arrives
def toznotify(STfeed, pin):
        GPIO.output(pin,GPIO.LOW)
        time.sleep(.1)
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(.1)
        # A number of stock 
        # n = notify2.Notification("New Torrent: ", STfeed.entries[0].title,
        #        "notification-message-im") # A stock icon name. For more icon
                                      # options, see icon.py in this folder.
        #n.show()
	return

def pwm(pin, angle):
    print "servo[" + str(pin) + "][" + str(angle) + "]"
    cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/servoblaster"
    os.system(cmd)
    #time.sleep(DELAY)
 
def FlashDesk():
    for j in range(0, 9999, STEP):
        pwm(0,j)
    time.sleep(DELAY)
    for j in range(9999, 0, (STEP*-1)):
        pwm(0,j)
    time.sleep(DELAY)
    pwm(0,0)
    time.sleep(2)

def lightsoff():
    os.system("echo 0=0 > /dev/servoblaster2")

STEP = 50
DELAY = 0.5

#blink GPIO17 50 times
#for i in range(0,10):
#       blink(11)
#GPIO.cleanup()

#Switch
#GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# SPI connection
#SCE  = 10 # gpio pin 24 = wiringpi no. 10 (CE0 BCM 8) - STB - 2ND END - STB
#SCLK = 14 # gpio pin 23 = wiringpi no. 14 (SCLK BCM 11) - SCK - 3RD END (MIDDLE) - SCK
#DIN  = 12 # gpio pin 19 = wiringpi no. 12 (MOSI BCM 10) -SIO - 1ST END - SIO

# Pin connections: VFD -> Pi
# Pin1 - GND -> GND
# Pin2 - Vcc -> 5V
# Pin3 - SI0 -> MOSI
# Pin4 - /STB -> CE0
# Pin5 - SCK -> CLK

## ST stuff

#Store the last item listed
STLastitem = ""
SecondToWait = 5
#RSS url feed link

#ALL
STurl = "http://www.sdfsadf.org/rssnew.php?passkey=sg&"
#xxx
#STurl = "http://www.dfsg.org/rssnew.php?passkey=dfg&cat=6&"
#STurl = "http://www.dfg.org/rssnew.ph0&type=desc&"




# data
COLS = 20
ROWS = 2

# commands
VFD_CLEARDISPLAY = 0x01
VFD_RETURNHOME = 0x02
VFD_ENTRYMODESET = 0x04
VFD_DISPLAYCONTROL = 0x08
VFD_CURSORSHIFT = 0x10
VFD_FUNCTIONSET = 0x20
VFD_SETCGRAMADDR = 0x40
VFD_SETDDRAMADDR = 0x80

# flags for display entry mode
VFD_ENTRYRIGHT = 0x00
VFD_ENTRYLEFT = 0x02
VFD_ENTRYSHIFTINCREMENT = 0x01
VFD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
VFD_DISPLAYON = 0x04
VFD_DISPLAYOFF = 0x00
VFD_CURSORON = 0x02
VFD_CURSOROFF = 0x00
VFD_BLINKON = 0x01
VFD_BLINKOFF = 0x00

# flags for display/cursor shift
VFD_DISPLAYMOVE = 0x08
VFD_CURSORMOVE = 0x00
VFD_MOVERIGHT = 0x04
VFD_MOVELEFT = 0x00

#01 = 0000 0001
#02 = 0000 0010
#04 = 0000 0100
#08 = 0000 1000
#10 = 0001 0000
#20 = 0010 0000
#40 = 0100 0000
#80 = 1000 0000

# flags for function set
VFD_8BITMODE = 0x10
VFD_4BITMODE = 0x00
VFD_2LINE = 0x08
VFD_1LINE = 0x00
VFD_BRIGHTNESS25 = 0x03
VFD_BRIGHTNESS50 = 0x02
VFD_BRIGHTNESS75 = 0x01
VFD_BRIGHTNESS100 = 0x00

VFD_5x10DOTS = 0x04
VFD_5x8DOTS = 0x00

VFD_SPICOMMAND = 0xF8
VFD_SPIDATA = 0xFA


def init():
    _displayfunction = VFD_8BITMODE
    begin(COLS, ROWS, _displayfunction, VFD_BRIGHTNESS100)

def begin(cols, lines, _displayfunction, brightness):
    if lines > 1:
       _displayfunction |= VFD_2LINE

    setBrightness(_displayfunction, brightness)

    _numlines = lines
    _currline = 0
    
    # Initialize to default text direction (for romance languages#include "SPI_VFD.h"
    _displaymode = VFD_ENTRYLEFT | VFD_ENTRYSHIFTDECREMENT 
    # set the entry mode
    command(VFD_ENTRYMODESET | _displaymode) 
  
    command(VFD_DISPLAYCONTROL | VFD_DISPLAYON)
    
    # go to address 0
    command(VFD_SETDDRAMADDR)  
    
    clear()
    home()
    
def display(_displaycontrol): 
    _displaycontrol |= VFD_DISPLAYON 
    command(VFD_DISPLAYCONTROL | _displaycontrol)  

def clear():
    command(VFD_CLEARDISPLAY)
    time.sleep(4)

def home():
    command(VFD_RETURNHOME)
    time.sleep(2)

def setBrightness(_displayfunction, brightness):
    #set the brightness (only if a valid value is passed
    if brightness <= VFD_BRIGHTNESS25: 
        _displayfunction &= ~VFD_BRIGHTNESS25
        _displayfunction |= brightness

    command(VFD_FUNCTIONSET | _displayfunction)

def setCursor(col, row):
    _numlines = 2
    row_offsets = [0x00, 0x40, 0x14, 0x54]
    if row > _numlines:
       row = _numlines-1        # count rows starting with 0
    print ("Sending cursor data :")
    command(VFD_SETDDRAMADDR | (col + row_offsets[row]) )

def noDisplay(vfdoff):
    command(VFD_DISPLAYCONTROL | vfdoff)


def text(string):
    #   display_char(ord(char))
    l = [VFD_SPIDATA]
    for char in string:
       l.append(ord(char))
    spi.writebytes(list(l))
    
       

def command(_setting):
    print _setting
    spi.writebytes([VFD_SPICOMMAND, _setting])
  
def shiftDisplay(rightOrLeft):
    command(VFD_CURSORSHIFT | VFD_DISPLAYMOVE | rightOrLeft) # = 0x18 or 0x1C

def msgToScreen(notification):
    text(notification)
    time.sleep(.5)
    for i in range(len(notification)*2):
        time.sleep(0.1)
        shiftDisplay(VFD_MOVELEFT)
    home()
    setCursor(1,1)
    time.sleep(3)
    clear()

# initalize SPI
spi = spidev.SpiDev()

spi.open(0,0)
spi.mode=3
spi.threewire
spi.max_speed_hz=500000

print("<==== Mainlline Starts ====>")
init()


print("<==== Print Text ====>")
while True:
    #rss feed
    STfeed = feedparser.parse( STurl )
    time.sleep(SecondToWait)
    if(len(STLastitem)>0):
        if(STLastitem != STfeed.entries[0].title):
            for i in range(0,5):
                FlashDesk()
            #blinkall()
            thistext = STfeed.entries[0].title
            thistext = thistext.replace("."," ")
            thistext = thistext.replace("_"," ")
            msgToScreen(thistext)
            lightsoff()
            #STLastitem = STfeed.entries[0].title
    else:
        for i in range(0,5):
            FlashDesk()
        msgToScreen("FUCK THIS ZERO BULLSHIT!!!")
        lightsoff()
        # espeak.synth("Hello there")
    STLastitem = STfeed.entries[0].title
    #time.sleep(5)



#noDisplay(VFD_DISPLAYOFF)
#time.sleep(5)
#noDisplay(VFD_DISPLAYON)
#clear()
#home()




#thistext = "See me Again!"
#text(thistext)
#clear()
#home()
print("<==== End of Program ====>")


