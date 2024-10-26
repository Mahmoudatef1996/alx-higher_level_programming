#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char >= 'a' and char <= 'z':
            new_char = chr(ord(char)-32)
        else:
            new_char = char
        print(new_char, end="")
    print()
