"""
This script demonstrate function decorators without argument
"""
def decorator_with_argument(arg1, arg2):
	print("Inside Decorator")
	def outer_wrapper(func):
		print("Inside __call__()")
		def wrapper():
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