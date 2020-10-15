"""Python multiprocessing star process id"""
import multiprocessing
import time
import os


def function5():
	print('Sub PPID and PID -->', os.getppid(), os.getpid())
	# p = multiprocessing.Process(target=function2)
	# p.start()

def function4():
	print('Sub PPID and PID -->', os.getppid(), os.getpid())
	p = multiprocessing.Process(target=function5)
	p.start()

def function3():
	print('Sub PPID and PID -->',os.getppid(), os.getpid())
	p = multiprocessing.Process(target=function4)
	p.start()

def function2():
	print('Sub PPID and PID -->', os.getppid(), os.getpid())
	p = multiprocessing.Process(target=function3)
	p.start()

def function1():
	print('Sub PPID and PID -->', os.getppid(), os.getpid())
	p = multiprocessing.Process(target=function2)
	p.start()

def main():
	print('Sub PPID and PID -->', os.getppid(), os.getpid())
	p = multiprocessing.Process(target=function1)
	p.start()


if __name__ == '__main__':
	main()
