# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:30:00 2018

@author: USER
"""

from pprint import pprint
import urllib.request, json
import numpy as np
url = "http://opendata2.epa.gov.tw/AQI.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
"""
print(len(data))

for i in range(0,len(data)-1):
       if str(data[i]['County']) == str("臺北市"):
              #pprint("ID: %d,   County: %s" %(i,data[i]['County']))
"""
#output="SiteName: %s, PM2.5: %s, PublishTime: %s" %(data[0]['SiteName'], data[0]['PM2.5'], data[0]['PublishTime'])
output=list([data[0]['SiteName'],data[0]['PM2.5'],data[0]['PublishTime'].replace(" ","-")])
#print(output)
exit(output)

