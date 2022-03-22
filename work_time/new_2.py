#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date = None):
    if start_date is None:
       start_date = date.today().replace(day = 17)
       _, days_in_month = calendar.monthrange(start_date.year,start_date.month)
       end_date = start_date + timedelta(days_in_month)
    return (start_date,end_date)

# a_day = timedelta(days = 4)
# first_day, last_day = get_month_range()
# while first_day < last_day:
    # print(first_day)
    # first_day += a_day 

def date_range(start,stop,step):
    while start < stop:
        yield start     
        start += step

for d in date_range(datetime(2019,5,4),datetime(2019,6,1),timedelta(days = 4):
    print(d)
    


