#!/usr/bin/python3
import requests
import datetime
import json

url = 'http://127.0.0.1:80/api/specificApis/studentData/signOutCron'
r = requests.get(url)
result = json.dumps(r.json())

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('./cron.log', 'a', encoding='utf-8') as f:
    f.write(now + '\n' + result + '\n')
