#asynchronous
import time
import asyncio
import aiohttp
def gettasks(session):
    tasks=[]
    for i in range(1,3):
        tasks.append(session.get(f"https://reqres.in/api/users?page{i}"))
        print(i, "done")
    return tasks
async def main():
    result=[]
    async with aiohttp.ClientSession() as session:
        tasks=gettasks(session)
        responses=await asyncio.gather(*tasks)
        for response in responses:
            result.append(await response.json())
start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
timetaken = time.time() - start
print('Time Taken {0}'.format(timetaken))