#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is in the range of lowercase letters (97 to 122)
    return 97 <= ord(c) <= 122

# Test the function
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('5'))  # False
