#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","test","test1234","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO tb_insert (logdata) VALUES ('Hello world');"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


####################
sql = "SELECT * FROM tb_insert"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      logdata = row[1]
      
      # Now print fetched result
      print "id=%s,logdata=%s" % \
             (id, logdata )
except:
   print "Error: unable to fecth data"


# disconnect from server
db.close()