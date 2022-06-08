#asynchronous
import time
import asyncio
import aiohttp
import json
def gettasks(session):
    tasks=[]
    for i in range(1,201):
        x=session.get(f'https://xkcd.com/{i}/info.0.json')
        tasks.append(x)
    return tasks
async def main():
    async with aiohttp.ClientSession() as session:
        tasks=gettasks(session)
        responses=await asyncio.gather(*tasks)
        i=0
        for response in responses:
            data_json = json.dumps(await response.json())
            with open(f"sample{i}.json", "w") as outfile:
                outfile.write(data_json)
                i=i+1
start = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

timetaken = time.time() - start
print('Time Taken {0}'.format(timetaken))