"""Mocule doc string"""
import time;
from datetime import timedelta


def main():
	str_time = '2018-07-17T12:57:29.000001Z'
	a = time.strptime(str_time,'%Y-%m-%dT%H:%M:%S.%fZ')
	b = time.localtime()
	# delta = b - a
	print('A ->', a.timedelta)
	# print('b ->', time.strftime(b))
	# print('C ->'. time.time())


if __name__ == '__main__':
	main()