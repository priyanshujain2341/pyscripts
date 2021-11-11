# Date: 11-11-2021
# Author: Priyanshu Jain
"""This scripts takes a bunch of reviews from  txt files located in a directory. It then converts each
of those reviews into a dictionary which is then sent to a server feedback REST end-point by parsing the 
dictionary into JSON format and making a POST request to the server."""

import os
import requests
from collections import OrderedDict


readpath = "/data/feedback/"
externalIp = "192.168.1.1"
url = "http://" +externalIp+ "/feedback"


def createDict(title, author, date, mbody):
	mydict = { "title": title, "name": author, "date": date, "feedback": mbody}
	#print(mydict)
	createRequest(mydict)

def createRequest(mydict):
	myrequest = requests.post(url, json = mydict)
	print("***")
	print(myrequest.request.body)
	response_code = myrequest.status_code
	print("---The HTTP response code was {}---".format(response_code))
	myrequest.raise_for_status()

for file in os.listdir(readpath):
	# print(os.path.join(readpath+file))
	with open(readpath+file,'r') as review:
		data = review.readlines()
		# print(data)
		createDict(data[0].rstrip(), data[1].rstrip(), data[2].rstrip(), data[3].rstrip())