# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:46:41 2019

@author: Miha
"""
import binascii
import set1_2
text = b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = b"ICE"
a = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"


def encrypt(txt, key):
    encrypted = ''
    for i in range(0, len(txt)):
        x = txt[i] ^ key[i % len(key)]        
        #print(key[i % len(key): (i % len(key)) + 2])
        tadd =  hex(x)[2:]
        if len(tadd) % 2 != 0:
            tadd = '0' + tadd
        encrypted += tadd
    return encrypted
b = encrypt(text, key)


    

