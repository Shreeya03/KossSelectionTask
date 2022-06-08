#synchronous
import time
import asyncio
import aiohttp
results=[]
def read(a,session):
    url=f"https://reqres.in/api/users?page{a}"
    response = session.get(url)
    return response
async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        for i in range(1,3):
            response=await read(i,session)
            results.append(await response.json())
            print(i, "done")
    timetaken = time.time() - start
    print('Time Taken {0}'.format(timetaken))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
