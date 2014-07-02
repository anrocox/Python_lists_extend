#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

How can join two into one list in python?

¿Como se pueden unir dos lista en una sola en python?
'''

#create two lists
lista1 = [9, 2, 5, 10, 9, 1, 3]
lista2 = ['a', 'b', 'c']
print (lista1)
print (lista2)

#create a new list result of using the + operator
lista3 = lista1 + lista2
print (lista3)

#Extend the list by adding all the items listed above
lista1.extend(lista2)
print (lista1)
