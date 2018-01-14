import sqlite3
import time
import os
db = sqlite3.connect('db.sqlite')
cursor = db.cursor()


def download_update():
  cursor.execute("DELETE FROM data")
  db.commit()
  cursor.execute("VACUUM")
  db.commit()
  cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='data'")
  db.commit()
  os.system("clear")
  print "Updating..."
  time.sleep(1)
  os.system("wget http://www.celestrak.com/NORAD/elements/noaa.txt")
  os.system("clear")
  print "Completed! \n"
  time.sleep(1)
  update_db()
  time.sleep(1)
  os.system("rm noaa*")
  os.system("clear")
  return
  
  
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
  
def sat_find():
 cursor.execute("SELECT COUNT(*) FROM data")
 sattelites = cursor.fetchall()
 raw_range = sattelites[0]
 rang = int(raw_range[0])
 print "Total DB objects count: " + str(range) + "\n"

 
 for list in range(rang):
  cursor.execute("SELECT name FROM data WHERE id=%d"%list)
  out = cursor.fetchall()
  print "--------------------------------"
  print "id: "+ str(list) + " name: " + str(out)[4:-20] + "\n"
  print "--------------------------------"
 time.sleep(2) 
 
def start_track(id):
  cursor.execute("SELECT name FROM data WHERE id=%d"%id)
  name = cursor.fetchall()
  cursor.execute("SELECT tle1 FROM data WHERE id=%d"%id)
  tle1 = cursor.fetchall()
  cursor.execute("SELECT tle2 FROM data WHERE id=%d"%id)
  tle2 = cursor.fetchall()
  tle = str(name)[4:-22] + "\n" + str(tle1)[4:-8] + "\n" +  str(tle2)[4:-8]
  #print str(tle)
  return tle
