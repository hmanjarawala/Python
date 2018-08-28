"""""
LinkedList Implementation
"""""
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
		
	def getData(self):
		return self.data
	
	def setData(self, value):
		self.data = value
		
	def getNext(self):
		return self.next
		
	def setNext(self, nextNode):
		self.next = nextNode

class LinkedList:
	def __init__(self, data):
	    node = Node(data)
	    self.head = node
	
	def append(self, data):
		node = Node(data)
		temp = self.head
		
		while(temp.next != None):
			temp = temp.next
		temp.next = node
	
	def insert(self, pos, data):
		node = Node(data)
		temp = self.head
		
		if pos == 0:
			self.head = node
			self.head.next = temp
		else:
			i=0
			while(i < pos and temp != None):
				i += 1
				prev = temp
				temp = temp.next
			if i == pos:
				prev.next = node
				node.next = temp
			else:
				raise IndexError("Overflow!")
	
	def __repr__(self):
	    s = ''
	    temp = self.head
	    while(temp.next != None):
	        s += "{data}->".format(data=temp.data)
	        temp = temp.next
	    s += "{data}".format(data=temp.data)
	    return s
		
if __name__ == '__main__':
	l = LinkedList(12)
	l.append(6)
	print(l)
	l.insert(0, 4)
	print(l)
	l.insert(2, 9)
	print(l)