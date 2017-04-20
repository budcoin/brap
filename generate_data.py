#!/usr/bin/env python

# USAGE
# $ python generate_data.py 67 69 110 98 5.2 1.1 0.9 1 1 2

import pymongo
from pymongo import MongoClient
from datetime import datetime
import sys

client = MongoClient()

db = client.brap_database
sessionsdata = db.sessionsdata

#datastring = sio.readline()
#sys.argv = datastring.split("'")
datarow = {
	"time" : datetime.utcnow(),
	"data" : {
		"tempf"  : sys.argv[1], 
		"tempr"  : sys.argv[2],
		"fronts" : sys.argv[3],
		"rears"  : sys.argv[4],
		"ax"     : sys.argv[5],
		"ay"	 : sys.argv[6],
		"az"	 : sys.argv[7],
		"gx"	 : sys.argv[8],
		"gy"	 : sys.argv[9],
		"gz"	 : sys.argv[10],

		}
	}

datarow_id = sessionsdata.insert_one(datarow).inserted_id
		

