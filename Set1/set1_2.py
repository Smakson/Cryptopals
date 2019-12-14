# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 21:00:55 2019

@author: Miha
"""
hex_dict = {
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            'a' : 10,
            'A' : 10,
            'b' : 11,
            'B' : 11,
            'c' : 12,
            'C' : 12,
            'd' : 13,
            'D' : 13,
            'e' : 14,
            'E' : 14,
            'f' : 15,
            'F' : 15       
            }


def hexdecode(inp):
    num = 0
    for c in inp:
        num = (num << 4) | hex_dict[c]
    return num


def xor(hx1, hx2):
    return hexdecode(hx1) ^ hexdecode(hx2)


