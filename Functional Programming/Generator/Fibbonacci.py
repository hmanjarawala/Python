"""
This script will generate fibonacci series using generators
"""
def fibbonacci(n):
	intNumber1 = 1
	intNumber2 = 0
	
	for i in range(n):
		yield intNumber1 + intNumber2
		intNumber2 = intNumber1 + intNumber2
		intNumber1 = intNumber2 - intNumber1

intNumber = 5
try:
	intNumber = int(input("Enter the number: "))
except ValueError:
	print("Entered value is not valid integer number")
	print("continue program with default value 5")

print("Fibbonacci searies: " + str(list(fibbonacci(intNumber))))