#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:00:05 2024

@author: satish
"""

# Define the three numbers
num1 = 10
num2 = 20
num3 = 30

# Calculate average of num1 and num2
avg1 = (num1 + num2) / 2

# Calculate average of num1 and num3
avg2 = (num1 + num3) / 2

# Calculate average of num2 and num3
avg3 = (num2 + num3) / 2

# Initialize a variable to store the highest average
highest_avg = avg1

# Check if avg2 is higher than the current highest average
if avg2 > highest_avg:
    highest_avg = avg2

# Check if avg3 is higher than the current highest average
if avg3 > highest_avg:
    highest_avg = avg3

# Print the highest average
print("Highest average of two numbers in the given set of three numbers:", 
      highest_avg)
