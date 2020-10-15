"""Python multiprocessing star process id"""
import multiprocessing
import time
import os

def function():
	"""Function Doc string"""
	print('Sub Process pid', os.getpid())
	time.sleep(1)

def main():
	"""Function Doc string"""
	print('Main Process pid', os.getpid())
	for i in range(0, 10):
		# name = 'p'+str(i)
		p = multiprocessing.Process(target=function)
		p.start()
		time.sleep(1)


if __name__ == '__main__':
	main()