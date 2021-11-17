# This script uploads all the images in the provided path to the webserver located at the given url

import requests
import os


mypath  = "C:/Users/Lenovo/Desktop/Converted/B/"
ip = "192.168.1.1"
url =  "http://" + ip + "/upload/"
# url = "https://ptsv2.com/t/kui39-1636872909/post/"



for file in os.listdir(mypath):
	if file.endswith(".jpeg"):	
		filename = os.path.join(mypath, file)
		# print(filename)
		with open (filename, 'rb') as opened:
			r = requests.post(url, files={'file': opened})
			print(r.status_code)