# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:20:15 2019

@author: Miha
"""
a = "7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f"
def chunkit_gen(inp, chunksize):
    return [inp[i:i + chunksize] for i in range(0, len(inp), chunksize)]


def counter(charray):
    count_dict = {}
    for ch in charray:
        if ch in count_dict:
            count_dict[ch] += 1
        else:
            count_dict[ch] = 1
    return count_dict


def ioc(charray, l):
    cnt = counter(charray)
    ic = 0
    for ch in cnt:
        ic += cnt[ch] * (cnt[ch] - 1)
    return ic/(l * (l - 1)/26)
    
with open("codes.txt", 'r') as file:
    lines = file.readlines()
    iocs = []
    i = 1
    for line in lines:
        charray = chunkit_gen(line, 2)
        iocs.append((ioc(charray, len(line)//2), i))
        i += 1
print(max(iocs, key = lambda x: x[0]))