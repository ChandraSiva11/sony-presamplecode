#Python Program to Compute Prime Factors of an Integer

def main():
	n =1780
	print("Factors are:")
	for i in range (1, n):
	    k = 0
	    if(n % i == 0):
	        for j in range(1, n):
	            if(i % j == 0):
	                k += 1
	        if(k == 2):
	            print(i)

if __name__ == '__main__':
	main()