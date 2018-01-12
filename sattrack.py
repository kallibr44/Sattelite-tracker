#!/usr/bin/env python
# -*- coding: utf-8 -*-

import predict
import json
import os
import time
qth = (56.5, 84.96667, 98)
tle = """NOAA 19 [+]
1 33591U 09005A   18011.92186191 +.00000120 +00000-0 +90276-4 0  9994
2 33591 099.1222 347.0149 0014775 048.2167 312.0264 14.12245172459856"""

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