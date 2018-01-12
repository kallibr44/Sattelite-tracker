import sqlite3
import time
db = sqlite3.connect('db.sqlite')
cursor = db.cursor()

def update_db():
  #f = open('noaa.txt', 'r')
  lines = 0
  i = 1
  y = 2
  z = 3
  name = ""
  tle1 = ""
  tle2 = ""
  cont = 0
  for line in open('noaa.txt'):

    lines += 1
  with open('noaa.txt', 'r') as f:
    for m in range(lines):
           if m == i:
            name = f.readline()
            i = i+3
	   elif m == y:
	    tle1= f.readline()
	    y = y+3
	   elif m == z:
	    tle2 = f.readline()
	    z = z+3
            cont = 1
	   if cont == 1:
      	     cursor.execute("""INSERT INTO data(name,tle1,tle2) VALUES('%(name)s','%(tle1)s','%(tle2)s')""" % {"name":name, "tle1":tle1 , "tle2":tle2 })
	     db.commit()
             cont = 0
	
  print "Lines: " + str(lines)
  db.close()
