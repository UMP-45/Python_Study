#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as pyplot

pyplot.plot(2,2)
scale = 'log'
pyplot.xscale(scale)
pyplot.yscale(scale)
pyplot.title('')
pyplot.xlabel('n')
pyplot.ylabel('run time(s)')
pyplot.show()