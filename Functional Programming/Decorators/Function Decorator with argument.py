"""
This script demonstrate function decorators without argument
"""
def decorator_with_argument(arg1, arg2):
	print("Inside Decorator")
	def outer_wrapper(func):
		print("Inside __call__()")
		def wrapper(): #Function without argument
			print("Entering into %s"%(func.__name__))
			print("Decorator called with %s %s"%(arg1, arg2))
			func()
			print("Exiting from %s"%(func.__name__))
		return wrapper
	return outer_wrapper

@decorator_with_argument('Hims',5)
def func1():
	print("Say Hello")

func1()
print("Again call decorator")
func1()

def myDecorator_with_argument(arg1, arg2):
	print("Inside Decorator")
	def outer_wrapper(func):
		print("Inside __call__()")
		def wrapper(*args): #Function with argument
			print("Entering into %s"%(func.__name__))
			print("Decorator called with %s %s"%(arg1, arg2))
			func(*args)
			print("Exiting from %s"%(func.__name__))
		return wrapper
	return outer_wrapper

@myDecorator_with_argument('Hims',5)
def sayHello(arg1, arg2, arg3):
	print("say Hello called with '%s' '%s' '%s'"%(arg1, arg2, arg3))

sayHello('say', 'Hello', 'Himansshu')
print("Again call decorator")
sayHello('say', 'Hello', 'to everyone')
