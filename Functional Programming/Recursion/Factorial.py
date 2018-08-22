"""""
This script will demonstrate to calculate factorial using function recursion
"""""
def factorial(n):
	#Base Value: 1! = 1
	if n == 1:
		return 1;
	else:
		return n * factorial(n-1)

intNumber = 5
try:
	intNumber = int(input("Enter the number: "))
except ValueError:
	print("Entered value is not valid integer number")
	print("continue program with default value 5")

print("Value of %d! is %d"%(intNumber, factorial(intNumber)))