#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    #Getter function
    @property
    def first_name(self):
        return self._first_name
   
    #Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
 
    #Delete function(optional)
    @first_name.deleter   
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person('Nanachi')
print(a.first_name)