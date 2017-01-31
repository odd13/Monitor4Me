import RPi.GPIO as GPIO
import time
import MySQLdb

# blinking function
def blink(pin):
       GPIO.output(pin,GPIO.LOW)
       time.sleep(1)
       GPIO.output(pin,GPIO.HIGH)
       time.sleep(1)
       return

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO tb_insert (logdata) VALUES ('"""+time.ctime()+"""');"""

def querietodb():
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
	return

# Open database connection
db = MySQLdb.connect("localhost","test","test1234","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel (LED)
led1 = 23
GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, GPIO.HIGH)

#blink GPIO17 50 times
#for i in range(0,10):
#       blink(11)
#GPIO.cleanup()


GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#input = GPIO.input(22)


while True:
  if (GPIO.input(22) == False):
    print "Gate Open: "+time.ctime()
    querietodb()
    blink(led1)
    time.sleep(.5)
  else:
    time.sleep(.5)

