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
 db.download_update()

def monitor(tle):
 #while True:
  raw_data = predict.observe(tle, qth)
  data=json.dumps(raw_data)
  p = predict.transits(tle, qth)
  for i in range(1,10):
	transit = p.next()
	print("%f\t%f\t%f" % (transit.start, transit.duration(), transit.peak()['elevation']))
  """
  raw_pred = predict.transits(tle, qth)
  pred = raw_pred.next()
  print "-------------------------------------------------------\n"
  print "Current sattelite: " + str(json.loads(data)['name']) + "\n"
  print "Latitude: " + str(json.loads(data)['latitude']) + "                          \n"
  print "Longitude: " + str(json.loads(data)['longitude']) + "                       \n"
  print "Next Transit: " + str(pred.start()\60\60\24)
  print "Transit duration: " + str(pred.duration()) + "\n"
  print "Transit Peak: " + str(pred.peak()['elevation']) + "\n"
  print "-------------------------------------------------------\n"
  time.sleep(0.5)
  os.system("clear") """
  
if __name__=='__main__':
 while True:
  print "-------------------------------------------------------\n"
  print "               Satelite Tracker (Beta)                 \n"
  print "                                                       \n"
  print "  1. Update TLE                                        \n"
  print "  2. Count DB                                          \n"
  print "  3. Start Track                                       \n"
  print "-------------------------------------------------------\n"
  choose = input("ST@local: ")
  if choose == 1:
   update()
  elif choose == 3:
   sat = input("Name of satelite: ")
   tle = db.start_track(sat)
   print "--------------------------------------\n"
   print "TLE Received! Starting track..."
   print tle
   time.sleep(2)
   monitor(tle)
  elif choose == 2:
   db.sat_find()
