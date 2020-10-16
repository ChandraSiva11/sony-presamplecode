"""Threading module doc string"""
import threading
import time


def function_a():
	while True:
		print('Function a called')
		time.sleep(1)


def function_b():
	while True:
		print('Function b called')
		time.sleep(1)

if __name__ == '__main__':
	t1 = threading.Thread(target=function_a)
	t2 = threading.Thread(target=function_b)
	t1.start()
	t2.start()