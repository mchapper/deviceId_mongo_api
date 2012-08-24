#!/usr/bin/python

from pymongo import Connection

connection = Connection('localhost', 27017)
device_profiles = connection['device_profiles']
user_devices = device_profiles['user_devices']
print user_devices.count()
		





