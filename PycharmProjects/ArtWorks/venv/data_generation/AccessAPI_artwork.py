import os
import csv
import json
import subprocess
from sys import argv
import time
from pprint import pprint

file_id = 0
source_file = '/Users/ravikiranmandha/PycharmProjects/ArtWorks/ArtWorks-dataset/Artwork/artwork_%d.txt' % file_id
target = open(source_file, 'w')

first_page = "'https://api.artsy.net/api/artworks'"
call_path = "curl -v %s -H 'X-Xapp-Token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU2MDcwMjcwNCwiaWF0IjoxNTYwMDk3OTA0LCJhdWQiOiI1Y2ZkMzQ2ZjFjODFhODAwMGVhZjUxZjMiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWNmZDM0NzBlNzBlODQwMDEyOWM4YzUyIn0.I990xqYdaXjwEf6yeOfWTCWJdBf_itib_Dml0ogRMa0='" % first_page
result = subprocess.check_output(call_path, shell=True)
json_output = json.loads(result)
artworks = json_output['_embedded']['artworks']
target.write(json.dumps(artworks))
time.sleep(.4)
file_id = file_id + 1
next_page = json_output['_links']['next']['href']
target.close()

while (next_page != ""):
    source_file = '/Users/ravikiranmandha/PycharmProjects/ArtWorks/ArtWorks-dataset/Artwork/artwork_%d.txt' % file_id
    target = open(source_file, 'w')
    call_path = "curl -v %s -H 'X-Xapp-Token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU2MDcwMjcwNCwiaWF0IjoxNTYwMDk3OTA0LCJhdWQiOiI1Y2ZkMzQ2ZjFjODFhODAwMGVhZjUxZjMiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWNmZDM0NzBlNzBlODQwMDEyOWM4YzUyIn0.I990xqYdaXjwEf6yeOfWTCWJdBf_itib_Dml0ogRMa0='" % next_page
    result = subprocess.check_output(call_path, shell=True)
    json_output = json.loads(result)
    artworks = json_output['_embedded']['artworks']
    target.write(json.dumps(artworks))
    time.sleep(.4)
    file_id = file_id + 1
    next_page = json_output['_links']['next']['href']
    target.close()