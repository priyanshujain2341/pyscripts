#!/usr/bin/env python3

"""This script uploads the data related to each of the fruits to the Django server"""

import os
import requests


path = "C:/Users/Lenovo/Desktop/Converted/A/"
ip = "192.168.1.1"
url = "http://" + ip + "/fruits/"


def createRequest(title, weight_string, description, file):
	weight = int(weight_string.split()[0])
	f, e = os.path.splitext(file)
	mydict = {"name": title, "weight": weight, "description": description, "image_name": f+".jpeg"}
	print(mydict)
	r = requests.post(url, mydict)
	print(r.status_code)
	# r.raise_for_status()


for file in os.listdir(path):
	filename = os.path.join(path, file)
	# print(filename)
	with open(filename, 'r') as opened:
		data = opened.readlines()
		createRequest(data[0].rstrip(), data[1].rstrip(), data[2].rstrip(), file)