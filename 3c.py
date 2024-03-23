#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:05:44 2024

@author: satish
"""

# Define the number to be checked
num = 12321

# Store the original number in a separate variable
original_num = num

# Initialize a variable to store the reversed number
reversed_num = 0

# Reverse the digits of the number
while num > 0:
    digit = num % 10  # Extract the last digit
    reversed_num = reversed_num * 10 + digit  # Append the digit to the reversed number
    num //= 10  # Remove the last digit from the original number

# Check if the reversed number is equal to the original number
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
