#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
5.17为起始日期，返回值为go
后两天返回值为true，
后三天
 1   2   3     4       5    6     7
 f   go  true  true    go   true  true
1  2 3 4 5  6 7
go t t f go t t
'''
from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date = None):
    if start_date is None:
       start_date = date.today().replace(day = 13)
       _, days_in_month = calendar.monthrange(start_date.year,start_date.month)
       end_date = start_date + timedelta(days_in_month)
    return (start_date,end_date)

a_day = timedelta(days = 2)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day 
    # first_day = a_day + timedelta(days = 2)
# for i in range(first_day,last_day):
    # print(first_day)
    # first_day = a_day + 2