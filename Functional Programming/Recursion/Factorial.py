"""""
This script will demonstrate to calculate factorial using function recursion
"""""
def factorial(n):
	#Base Value: 1! = 1
	if n == 1:
		return 1;
	else:
		return n * factorial(n-1)

print("Value of 5! is %d"%(factorial(5)))