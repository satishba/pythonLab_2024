#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:41:04 2024

@author: satish
"""

#Print the fibonacci series

# Initialize the first number in the Fibonacci sequence
num1 = 0  

# Initialize the second number in the Fibonacci sequence
num2 = 1  

# Print the first number in the sequence
print(num1)  

# Print the second number in the sequence
print(num2)  

# Loop to generate the Fibonacci sequence up to the 10th term
for i in range(1, 10):
    # Calculate the next number in the sequence by adding the previous two numbers
    num3 = num1 + num2  
    
    # Print the next number in the sequence
    print(num3)  
    
    # Update the first number to be the value of the second number for the next iteration
    num1 = num2  
    
    # Update the second number to be the value of the next number in the sequence for the next iteration
    num2 = num3  

    