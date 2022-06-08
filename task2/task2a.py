#synchronous
import json
import time
import requests
start = time.time()
for i in range (1,201):
    url='https://xkcd.com/{}/info.0.json'.format(i)
    response=requests.get(url).json()
    data_json = json.dumps(response)
    with open(f"sample{i}.json", "w") as outfile:
        outfile.write(data_json)
timetaken = time.time() - start
print('Time Taken {0}'.format(timetaken))