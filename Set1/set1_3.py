# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 21:50:06 2019

@author: Miha
"""
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
        'z' : 0.00074
        }

sort_dict = sorted(freq_dict.items(), key = lambda x: x[1])



def chunkit_gen(inp, chunksize):
    if len(inp) % chunksize != 0:
        def gen():
            yield from (inp[i:i + chunksize] for i in range(0, len(inp), chunksize))
            yield inp[len(inp) - chunksize - 1:]
        return gen
    return (inp[i:i + chunksize] for i in range(0, len(inp), chunksize))


def counter(chararray, length, low_eq_up = True):
    count_dict = {}
    for char in chararray:
        if char in count_dict:
            count_dict[char.lower()] += 1
        else:
            count_dict[char.lower()] = 1
    for c in count_dict:
        count_dict[c] /= length
    return count_dict
    

def freq_analysis(crypto_str, charsize, length, ref_dict = freq_dict):
    count = counter(chunkit_gen(crypto_str, charsize), length)
    sort_count = sorted(count.items(), key = lambda x: x[1])
   # print(sort_count)
    return sort_count, {sort_count[-i][0] : sort_dict[-i][0] for i in range(len(sort_count))}


def decode(encoded, mapping):
    decoded = ''
    print(mapping)
    for i in range(0, len(encoded), 2):
        print(encoded[i:i+2])
        decoded += mapping[encoded[i:i + 2]]
    return decoded


def cryptanalyse(crypted):
    counted, maps = freq_analysis(crypted, 2, len(crypted)//2)
    print(counted)
    for i in range(len(counted)):
        most_common = counted[-i][0]
        code = hex(set1_2.xor(most_common, '65'))[2:]
        print(code)
        decoded = ''
        for j in range(0, len(crypted), 2):
            dechr = set1_2.xor(code, crypted[j:j+2])
            decoded += chr(dechr)
        print(decoded)
    

    
    