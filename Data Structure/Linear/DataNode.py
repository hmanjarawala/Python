# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:25:33 2020

@author: Himanshu.Manjarawala
"""

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