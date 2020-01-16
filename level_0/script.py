#!/usr/bin/python3
import requests
ENDPOINT = "http://158.69.76.135/level0.php"
data = {"id" : "830", "holdthedoor" : "Submit+Query"}
for i in range(0, 1024):
	requests.post(url = ENDPOINT, data = data)