#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:09:08 2024

@author: satish
"""

year=1999

if ( (year % 4 ==0 and year % 100 != 0 ) or year % 400 ==0) :
    print(f"{year} is leap")
else :
    print(f"{year} is not leap")