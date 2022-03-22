#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property 
    def area(self):
        return math.pi * self.radius **2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius, c.area, c.perimeter)
