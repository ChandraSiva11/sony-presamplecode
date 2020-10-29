import asyncio
import time

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
# asyncio.run(main())


async def fun1():
	while True:
		print("Hello .....")
		await asyncio.sleep(1)
		# time.sleep(1)

async def fun2():
	while True:
		print("..... World")
		await asyncio.sleep(1)
		# time.sleep(1)

if __name__ == "__main__":
	loop1 = asyncio.fun1()
	task1 = loop1.create_task(fun1())

	loop2 = asyncio.fun2()
	task2 = loop1.create_task(fun2())

	loop1.run_until_complete(asyncio.wait([task1, task2])
	# task1.close()
	# task2.close()