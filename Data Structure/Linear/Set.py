# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:27:09 2020

@author: Himanshu.Manjarawala
"""

#A set is a collection which is unordered and unindexed.
#Create a set
my_set = {"apple", "banana", "cherry"}
print(my_set)

#Access Items
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
for item in my_set:
    print(item)

#Check if item exists in the set
if "cherry" in my_set:
    print("Yes, cherry exists in the fruit set")

#Change items
#Once a set is created, you cannot change its items, but you can add new items.

#Add Items
#To add one item to a set use the add() method.
my_set.add("orange")
print(my_set)

#To add more than one item to a set use the update() method.
my_set.update(["mango","grapes"])
print(my_set)

#Length of Set
print(len(my_set))

#Remove Item from Set
my_set.remove("orange")
print(my_set)

#If the item to remove does not exist, remove() will raise an error.
try:
    my_set.remove("jeckfruit")
except Exception as e:
    print("""trying remove \"jeckfruit\" from 
          Set which is not present. Hence throw an exception {}""".format(e))

#If the item to remove does not exist, discard() will NOT raise an error.
try:
    my_set.discard("jeckfruit")
    print("discard() method doesn't throw exception")
except Exception as e:
    print("""trying remove \"jeckfruit\" from 
          Set which is not present. Hence throw an exception {}""".format(e))

#You can also use the pop(), method to remove an item, but this method will remove the last item. 
#Remember that sets are unordered, so you will not know what item that gets removed.
x = my_set.pop()
print(x)

#Clear Set Items
my_set.clear()
print(my_set)

#Join Two set
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

#Difference between sets
#Returns a set containing the difference between two or more sets
set3 = set1.difference(set2)
print(set3)

#Removes the items in this set that are also included in another, specified set
set1.difference_update(set2)
print(set1)

#Returns a set, that is the intersection of two other sets
set1.update(set2)
set3 = set1.intersection(set2)
print(set3)

#Removes the items in this set that are not present in other, specified set(s)
set1.intersection_update(set2)
print(set1)