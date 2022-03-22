#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from datetime import timedelta
from datetime import datetime

parser = argparse.ArgumentParser(description = 'get today')
parser.add_arg ument('-t','--today',help = 'enter today')
args = parser.parse_args()

#将输入的参数格式化
text = args.today
get = datetime.strptime(text,'%Y-%m-%d')

d = datetime(2019,5,18)
out = get - d
print(out)

#取模判断
outdays = out.days % 4
if outdays == 0 or outdays == 1:
    print(True)
else :print(False)