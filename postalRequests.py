#!/usr/bin/python3

import os
import requests

web_adress = 'http://EDIT_THIS'
headers = {'Content-Type':'application/json'}
dirname = "EDIT_THIS "

for filename in os.listdir(dirname):
    print(filename)
    file_path = os.path.join(dirname, filename)
    with open(file_path, 'r') as json_data:
        r = requests.post(web_adress, data=json_data, headers=headers)
        print(r.text)
