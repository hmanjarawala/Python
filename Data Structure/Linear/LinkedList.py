"""""
LinkedList Implementation
"""""

from DataNode import Node

class LinkedList:
    
    __count = 1
    
    def __init__(self, data):
	    node = Node(data)
	    self.head = node
    
    def __iter__(self):
        return self
    
    def __next__(self):
        temp = self.head
        if(temp == None):
            raise StopIteration("End of LinkedList")
        self.head = self.head.next
        return temp.data
    
    def append(self, data):
        node = Node(data)
        temp = self.head
        
        while(temp.next != None):
            temp = temp.next
        temp.next = node
        self.__count+=1
    
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
        self.__count+=1
    
    def __getitem__(self, index):
        if index == 0:
            return self.head
        elif self.__count <= index:
            raise IndexError("Overflow!")
        else:
            i=0
            temp = self.head
            while(i < index and temp != None):
                i += 1
                temp = temp.next
            
            if i == index:
                return temp.data
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


def main():
    l = LinkedList(12)
    l.append(4)
    l.insert(0, 6)
    l.insert(2,9)
    print(l)
    print(l[3])
    print(l[4])
    
    for x in l:
        print(x)
		
if __name__ == "__main__":
    main()