"""
This script demonstrate function decorators without argument
"""
def entry_exit(func):
	print("Inside Decorator")
	def wrapper():  #function without arguments
		print("Entering into %s"%(func.__name__))
		func()
		print("Exiting from %s"%(func.__name__))
	return wrapper

@entry_exit
def func1():
	print("Called inside decorator function")

func1()

def myDecorator(func):
	print("Inside Decorator")
	def wrapper(*args):
		print("Entering into %s function with argument"%(func.__name__))
		func(*args)
		print("Exiting from %s function with argument"%(func.__name__))
	return wrapper

@myDecorator
def sayHello(arg1, arg2, arg3):
	print("Function sayHello called with '%s' '%s' '%s'"%(arg1, arg2, arg3))

	
sayHello('say', 'Hello', 'Himansshu')