#!/usr/bin/python
# -*- coding: utf-8 -*-

import predict
import json
import os
import time
import db

os.system("clear")
qth = (56.5, 84.96667, 98)
tle = """NOAA 19 [+]
1 33591U 09005A   18011.92186191  .00000120  00000-0  90276-4 0  9994
2 33591  99.1222 347.0149 0014775  48.2167 312.0264 14.12245172459856"""

def update():
  os.system("clear")
  print "Updating..."
  time.sleep(1)
  os.system("wget http://www.celestrak.com/NORAD/elements/noaa.txt")
  os.system("clear")
  print "Completed! \n"
  time.sleep(1)
  db.update_db()
  time.sleep(1)
  os.system("rm noaa*")
  os.system("clear")
  return

def monitor():
 while True:
  raw_data = predict.observe(tle, qth)
  data=json.dumps(raw_data)
  print "-------------------------------------------------------\n"
  print "Current sattelite: " + str(json.loads(data)['name']) + "\n"
  print "Latitude: " + str(json.loads(data)['latitude']) + "                          \n"
  print "Longitude: " + str(json.loads(data)['longitude']) + "                       \n"
  print "-------------------------------------------------------\n"
  time.sleep(0.5)
  os.system("clear")
  
if __name__=='__main__':
 print "-------------------------------------------------------\n"
 print "               Satelite Tracker (Beta)                 \n"
 print "                                                       \n"
 print "  1. Update TLE                                        \n"
 print "  2. Start Track                                       \n"
 print "-------------------------------------------------------\n"
 choose = input("ST@local: ")
 if choose == 1:
  update()
 elif choose == 2:
  #sat = input("Name of satelite: ")
  print "Start locating NOAA19"
  time.sleep(2)
  monitor()
 
