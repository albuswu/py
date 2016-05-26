#! /usr/bin/python

import json
import time
from pprint import pprint

#start = time.time()

with open("json_files/foo.json") as json_file:
	json_data = json.load(json_file)["results"][0]["result"]["tag"]
	# Prints out the different classes in the picture
	classes = json_data["classes"]
	prob = json_data["probs"]
	pprint(classes)
	pprint(prob)
	assert len(classes) == len(prob), "match"
	
	car = False
	index = 0
	for i in range(len(classes)):
		if classes[i] == 'car':
			car = True
			index = i
	if car and prob[index] > 0.8:
		print "Car Passed"
		print prob[index]

#print str(time.time() - start) + ' seconds'

