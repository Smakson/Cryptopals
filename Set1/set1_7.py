# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 06:14:50 2019

@author: Miha
"""

keystr = "YELLOW SUBMARINE"
keybytes = bytes(keystr, 'ascii')
irred = 0b100011011

def csl(x, shift):
    """Circular left shift on an 8-bit number"""
    return (x << shift) | (x >> (8 - shift))

def affine(x):
    return x ^ (csl(x, 1)) ^ (csl(x, 2)) ^ (csl(x, 3)) ^ (csl(x, 4)) ^ 0x63

def inv_affine(x):
    return (csl(x,1)) ^ (csl(x,3)) ^ (csl(x, 6)) ^ 0x5

def mult_inv_table_init():
    table = [[0 for j in range(16)] for i in range(16)]
    
    
    
def aes128_ecb_decrypt(bytestream, key):
    pass
    