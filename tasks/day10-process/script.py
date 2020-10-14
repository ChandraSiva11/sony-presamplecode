"""Module doc string"""
from packages1.pak1_mod1 import pk1_func1, pk1_func2
from packages1.pak1_mod2 import pk1_func11
import packages1.pak1_mod3 as a
# import packages1.pak1_mod3

from packages2.pak2_mod1 import pk2_func1, pk2_func2
from packages2.pak2_mod2 import *
import packages2.pak2_mod3 as b
# import packages2.pak2_mod3

def main():
	print('\nScript Main function called\n')
	
	# Package 1 modules and function calling
	pk1_func1()
	pk1_func2()

	pk1_func11()
	# pk1_func22()  # It can't be called because it is not imported from packages1 module2

	a.pk1_func111() 	# This function not imported sucessfully from the package1 maodule3
	# pk1_func222() 	# This function not imported sucessfully from the package1 maodule3

	#--------------------------------------------------------------------------------------

	# Package 2 Modules and function calling
	pk2_func1()
	pk2_func2()

	pk2_func11()
	pk2_func22()

	b.pk2_func111()
	# pk2_func222() 	# Error it is not imported sucessfully


if __name__ == '__main__':
	main()
