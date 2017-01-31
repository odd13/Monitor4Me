import RPi.GPIO as GPIO
import time
import MySQLdb
from time import gmtime, strftime
import feedparser

# blinking function
def blink(pin):
       GPIO.output(pin,GPIO.LOW)
       time.sleep(.1)
       GPIO.output(pin,GPIO.HIGH)
       time.sleep(.1)
       return
   
def blinkall():
    for x in range(15):
        blink(led1)
        blink(led2)
        blink(led3)
        blink(led4)
    return

def querietodb():
    # Prepare SQL query to INSERT a record into the database.
	sql = """INSERT INTO tb_insert (logdata) VALUES ('"""+time.ctime()+"""');"""
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
	return

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



# Open database connection
db = MySQLdb.connect("localhost","test","test1234","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel (LED)
led1 = 23
led2 = 24
led3 = 22
led4 = 18
GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, GPIO.HIGH)

GPIO.setup(led2, GPIO.OUT)
GPIO.output(led2, GPIO.HIGH)

GPIO.setup(led3, GPIO.OUT)
GPIO.output(led3, GPIO.HIGH)

GPIO.setup(led4, GPIO.OUT)
GPIO.output(led4, GPIO.HIGH)
#blink GPIO17 50 times
#for i in range(0,10):
#       blink(11)
#GPIO.cleanup()

#this was switch
#GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Store the last item listed
STLastitem = ""
SecondToWait = 15
#RSS url feed link

#ALL
#STurl = "http://www.supertorrents.org/rssnew.php?passkey=b5aa6c968012df1b6f0ffe2288913246&"
#xxx
#STurl = "http://www.supertorrents.org/rssnew.php?passkey=b5aa6c968012df1b6f0ffe2288913246&cat=6&"
STurl = "http://www.supertorrents.org/rssnew.php?passkey=b5aa6c968012df1b6f0ffe2288913246&act=free&sort=0&type=desc&"


while True:
    #rss feed
    #STfeed = feedparser.parse( STurl )
    #time.sleep(SecondToWait)
    
    #if(STLastitem != STfeed.entries[0].title):
        blinkall()
    #    print STfeed.entries[0].title + strftime("%X", gmtime()) + " - " +  STLastitem
    #    STLastitem = STfeed.entries[0].title

	




#while True:
#  if (GPIO.input(22) == False):
#    print "Gate Open: "+time.ctime()
#    querietodb()
#    blink(led1)
#    blink(led2)
#    blink(led3)
#    blink(led4)
#  else:
#    time.sleep(.5)




