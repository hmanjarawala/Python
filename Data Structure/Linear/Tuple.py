# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:42:51 2020

@author: Himanshu.Manjarawala
"""

#Create tuple
my_tuple = ("apple", "banana",  "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple)

#Access tuple item
#Remmber tuple starts with 0
print(my_tuple[1])

# Negative index -1 return last item
print(my_tuple[-2]) #return 2nd last item

#Range of Indexes
print(my_tuple[2:5]) #return 3rd, 4th & 5th item.

print(my_tuple[:4]) #from begining to index 4

print(my_tuple[2:]) #from index 2 to end of tuple

#Renge of negative index
print(my_tuple[-4:-1]) #returns the items from index -4 (included) to index -1 (excluded)

#Loop through tuple
for item in my_tuple:
    print(item)

#Check if item exists in the tuple
if "mango" in my_tuple:
    print("Yes, mange exists in the fruit tuple")

#Length of tuple
print(len(my_tuple))

#Add Item
try:
    my_tuple[len(my_tuple)] = "blackcurrent"
except Exception:
    print("can't add item to tuple as it is unchangable.")

#Add item in tuple
temp_list = list(my_tuple)
temp_list.append("blackcurrent")
my_tuple = tuple(temp_list)
print(my_tuple)

#Create tuple with one item
single_tuple = ("single",)
print(type(single_tuple))

single_tuple = ("single")
print(type(single_tuple)) #Not a tuple

#Join Two Tuples
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
my_tuple = tuple1 + tuple2
print(my_tuple)