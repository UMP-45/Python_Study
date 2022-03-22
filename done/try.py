#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
    print("Oops!  That was no valid number.  Try again...")