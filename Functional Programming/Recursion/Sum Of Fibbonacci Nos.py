"""""
This script will calculate nth fibbonacci numbers
"""""
def fibbonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibbonacci(n-1) + fibbonacci(n-2)

intNumber = 5
try:
	intNumber = int(input("Enter the number: "))
except ValueError:
	print("Entered value is not valid integer number")
	print("continue program with default value 5")

print("Value of %dth fibbonacci number is %d"%(intNumber+1, fibbonacci(intNumber)))