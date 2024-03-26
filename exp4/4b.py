#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:21:14 2024

@author: satish
"""
# Find if a given number is prime or not .

num=21
prime=0
for i in range(2,num):
    if num % i == 0 :
        prime=1
if prime == 0:
    print(f"{num} is prime")
else :
    print(f"{num} is not prime")
    