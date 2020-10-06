import requests
import datetime
import json

url = 'http://121.196.42.250/api/specificApis/studentData/signOutCron'
r = requests.get(url)
result = json.dumps(r.json())

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('./cron.log', 'a', encoding='utf-8') as f:
    f.write(now + '\n' + requests + '\n')