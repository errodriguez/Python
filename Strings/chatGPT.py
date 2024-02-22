#!/usr/bin/env python

def is_valid_string(s):
    char_count = {}
    
    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    values = list(char_count.values())
    
    # Check if all values are evenly distributed
    if all(value == values[0] for value in values):
        return True
    
    # Check if removing one character makes the rest evenly distributed
    for i in range(len(values)):
        if values[i] > 1:
            values[i] -= 1
            if all(value == values[0] for value in values):
                return True
            values[i] += 1
    
    return False

# Test cases
input_string = input("Enter a string: ")
if is_valid_string(input_string):
    print("Valid string")
else:
    print("Invalid string")
