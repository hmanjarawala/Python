# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:00:01 2020

@author: Himanshu.Manjarawala
"""

# Define List
my_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(my_list)

# Access Item
# Remember Lists start from 0
print(my_list[2]) #return 3rd Item

# Negative index -1 return last item
print(my_list[-2]) #return 2nd last item

#Range of Indexes
print(my_list[2:5]) #return 3rd, 4th & 5th item.

print(my_list[:4]) #from begining to index 4

print(my_list[2:]) #from index 2 to end of list

#Renge of negative index
print(my_list[-4:-1]) #returns the items from index -4 (included) to index -1 (excluded)

#Loop through list
for item in my_list:
    print(item)

#Check if item exists in the list
if "mango" in my_list:
    print("Yes, mange exists in the fruit list")

#Length of List
print(len(my_list))

#Add Item in the list
#Add item at the end of list
my_list.append("blackcurrent")
print(my_list)

#Add item at given index
my_list.insert(1, "jeckfruit")
print(my_list)

#Remove item
my_list.remove("jeckfruit")
print(my_list)

#remove item from perticular index or last item if index not specified
my_list.pop()
print(my_list)

#remove specified index from list
del my_list[0]
print(my_list)

#clear method empties the list
my_list.clear()
print(my_list)

#delete entire list
del my_list
#print(my_list)

#Copy a list
my_list = ["apple", "banana", "mango"]
copy_list = my_list.copy()
print(copy_list)

#another way to copy list
copy_list = list(my_list)
print(copy_list)

#Join Two Lists
list1 = ["a","b","c"]
list2 = [1,2,3]
my_list = list1 + list2
print(my_list)

#use extend method
list1.extend(list2)
print(list1)