"""""
Stack Implementation
"""""
class stack:
	
	def __init__(self, *args, **kwargs):
	    
	    if len(args) == 1:		    
	        foundOneArg = True;		    theOnlyArg = args[0]
	    else:           		
		    foundOneArg = False;	    theOnlyArg = None
		
	    if foundOneArg and isinstance(theOnlyArg, list):
		    self.__data = [x for x in theOnlyArg]
	    elif foundOneArg and isinstance(theOnlyArg, stack):
		    self.__data = [x for x in theOnlyArg.__data]
	    else:
		    self.__data = [x for x in args]
		    
	
	def push(self, value):
		self.__data.append(value)
	
	def pop(self):
	    try:
	        return self.__data.pop(-1)
	    except IndexError as e:
	        return e
		
	def __repr__(self):
		s1 = "|{}|\n".format("-"*len(str(max(self.__data))))
		for i in self.__data[::-1]:
			s1 = s1 + "|" + str(i) + "|\n"
			s1 = s1 + "|{}|\n".format("-"*len(str(max(self.__data))))
		return s1
	
	def __getitem__(self, index):
	    try:
	        return self.__data[index]
	    except IndexError as e:
	        return e
		
		
s = stack()
s.push(34)
s.push(59)
s.push(21)
print(s)
print(s.pop())
s.push(45)
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s = stack([23,45,67])
print(s)
print(s[2])
print(s[3])