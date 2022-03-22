#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
with open('good.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)
print(row[0])
print(row[1])
print(row)