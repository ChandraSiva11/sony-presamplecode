"""Module doc string"""
from packages1.module_a import func_l, func_m
from packages1.module_b import func_n

from packages2.module_c import func_p
from packages2 import func_r
# from packages2.module_d import *


def main():
	print('\nScript Main function called\n')
	func_l()
	func_m()

	func_n()
	# func_o()

	func_p()
	# func_q()

	func_r()
	# func_s()


	

if __name__ == '__main__':
	main()
