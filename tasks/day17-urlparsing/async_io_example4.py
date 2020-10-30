import asyncio
import time

async def say_after(delay, what):
    while True:
    	await asyncio.sleep(delay)
    	print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    while True:
	    await say_after(1, 'hello')
	    await say_after(1, 'world')
	    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())