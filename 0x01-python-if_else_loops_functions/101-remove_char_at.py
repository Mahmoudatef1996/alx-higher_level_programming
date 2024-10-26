#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_str = ''
    for c in str:
        if n == i:
            i = i + 1
        else:
            new_str += c
            i = i + 1
    return new_str
