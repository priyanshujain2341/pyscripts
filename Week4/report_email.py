#!/usr/bin/env python3

import os
import datetime
import reports

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

def generate_pdf(path):
	body = ""
	for file in os.listdir(path):
		if file.endswith(".txt"):
			with open (path+	file, 'r') as opened:
				data = opened.readlines()
				body += "name: " + data[0] + "<br/>" + "weight: " + data[1] + "<br/><br/>"

	return body

if __name__ == "__main__":
	path = "C:/Users/Lenovo/Desktop/Converted/A/"
	title = "Processed Update on " + current_date
	data = generate_pdf(path)
	reports.generate_report("/tmp/processed.pdf", title, data)

	# generate email information
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ["USER"])
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	attachment = "/tmp/processed.pdf"

	message = emails.generate_email(sender, receiver, subject, body, attachment)
	emails.send_email(message)