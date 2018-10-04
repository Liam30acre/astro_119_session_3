import numpy as np
import sys

#define a function that returns a value 
def expo(x):
	return np.exp(x)	#return the np e^x function
	
#define a subroutine that does not return a value 
def show_expo(n):
	for i in range(n):	# i=[0,n-1]
		print(expo(float(i)))	#call the expo function

def main():
	n = 10 #default # for n
	
	#check if there is a command line argument provided 
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#if an argument was provided use it for n, use [1] bc 
								#0 is the first input on command line and 1 is 2nd input
		
	show_expo(n)	#call the show_expo subroutine
	
#run main function
if __name__ == "__main__":
	main()
	