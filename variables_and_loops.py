import numpy as np

def main():
	i = 0	#integer
	n = 10
	x = 119.0	#floating point num declared w a "."
	
	# we use numpy to declare arrays quickly 
	
	y = np.zeros(n,dtype=float) #declares 10 zeros as floats using np
	
	#we can iterate through the elements of y by passing an index
	
	for i in range(n): #i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1.0 # set y = 2i+1 as float
		
	#we can also iterate through an array 
	for y_element in y:
		print(y_element)
		
	#execute the main function
if __name__ == "__main__":
	main()
	 