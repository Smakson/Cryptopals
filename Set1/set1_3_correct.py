# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 23:26:33 2019

@author: Miha
"""
import math
import set1_2
mystery = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

mysterstring = bytearray.fromhex(mystery).decode('ascii')

freq_dict = {
        'e' : 0.12702,
        't' : 0.09056,
        'a' : 0.08167,
        'o' : 0.07507,
        'i' : 0.06966,
        'n' : 0.06749,
        's' : 0.06327,
        'h' : 0.06094,
        'r' : 0.05987,
        'd' : 0.04253,
        'l' : 0.04025,
        'c' : 0.02782,
        'u' : 0.02758,
        'm' : 0.02406,
        'w' : 0.02360,
        'f' : 0.02228,
        'g' : 0.02015,
        'y' : 0.01974,
        'p' : 0.01929,
        'b' : 0.01492,
        'v' : 0.00978,
        'k' : 0.00772,
        'j' : 0.00153,
        'x' : 0.00150,
        'q' : 0.00095,
        'z' : 0.00074,
        'sp' : 0
        }

sort_dict = sorted(freq_dict.items(), key = lambda x: x[1], reverse = True)



def xor_string(st1, st2):
    xored = ''
    if len(st1) != len(st2):
        return False
    for i in range(len(st1)):
        xored += chr(ord(st1[i]) ^ ord(st2[i]))
    return xored



def xor_chr(st, char):
    xored = ''
    for i in range(len(st)):
        xored += chr(ord(st[i]) ^ ord(char))
    return xored


def score(st):
    sc = 100
    l = len(st)
    count_dict = {c : 0 for c in freq_dict}
    for c in st:
        if not c.isalnum() and c != ' ' :
            count_dict['sp'] += 1
        elif not c.isascii():
            count_dict['sp'] += 1
        elif c.lower() in count_dict:
            count_dict[c.lower()] += 1
        else:
            count_dict[c.lower()] = 1
    for ch in freq_dict:
        if ch in count_dict:
            sc -= ((freq_dict[ch] * l -  count_dict[ch]))**2
        else:
            sc -= (freq_dict[ch]*l)**2

    return sc


def cryptanalyse(encrypted):
    max_score = - math.inf
    bst_cd = 0
    for i in range(256):
        codechr = chr(i)
        xored = xor_chr(encrypted, codechr)
        scr = score(xored)
        
        if scr > max_score:
            max_score = scr
            bst_cd = i
    return (bst_cd, xor_chr(encrypted, chr(bst_cd)), max_score)
        
        

            
            
        
        




