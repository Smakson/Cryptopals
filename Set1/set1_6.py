# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 23:30:48 2019

@author: Miha
"""
import math
import base64
import set1_3_correct
import set1_5
def hamming_chr(a, b):
    count = 0
    d = a ^ b
    bd = bin(d)
    for i in range(len(bd)):
        if bd[i] == '1':
            count += 1
    return count

def hamming_str(a, b):
    la = len(a)
    lb = len(b)
    if la != lb:
        return 0
    count = 0
    
    for i in range(len(a)):
        count += hamming_chr(a[i], b[i])
    return count


def decrypt_vigener(cryptext):
    crypbytes = str.encode(cryptext)
    #print(crypbytes)
    len(crypbytes)
    scores = []
    for keysize in range(2, 40):
        chunked = [crypbytes[i: i +keysize] for i in range(0, len(crypbytes), keysize)]
        if len(crypbytes) % keysize != 0:
            chunked += [crypbytes[len(crypbytes) - keysize - 1:]]
        
        dist = 0
        
        for i in range(1, len(chunked), 2):
            
            dist += hamming_str(chunked[i - 1], chunked[i])/keysize
        scores.append((dist/(len(crypbytes)//keysize), keysize))
    sorts = sorted(scores, key = lambda x: x[0])
    print(sorts)
    keysizes = [sorts[0][1], sorts[1][1], sorts[2][1]]
    decrypts = []
    for keysz in keysizes:
        blocks = [([crypbytes[j] for j in range(len(crypbytes)) if j % keysz == i]) for i in range(keysz)]    
        codes = []
        strs = []
        #decors = []
        for bl in blocks:
            st = ''
            for i in bl:
                st += chr(i)
            strs.append(st)
            code, decrypted, scor = set1_3_correct.cryptanalyse(st)
            codes.append(chr(code))
            #print(scor)
            #decors.append(decrypted)
        #return strs
        code = ''.join(codes)
        print(code)
        codebytes = str.encode(code)
        #return decors
        decrypts.append(set1_5.encrypt(crypbytes, codebytes))
    return decrypts
        
    
crypto = ''

with open("challenge6_crypto.txt", 'r') as file:
    for line in file.readlines():
        line = line.strip('\n')
        crypto += base64.b64decode(line).decode('ascii')

lel = decrypt_vigener(crypto)

        

        
