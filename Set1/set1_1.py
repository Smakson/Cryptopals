# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:48:40 2019

@author: Miha
"""


def bytetobits(bytes3):
    return (bytes3[0] << 16) | (bytes3[1] << 8) | bytes3[2]
    
    
def bytes2base(bytes3):
    bits = bytetobits(bytes3)
    groups = [(bits >> 18 )& 0x3f, (bits >> 12) & 0x3f, (bits >> 6) & 0x3f, bits & 0x3f]
    base = ''
    for group in groups:
        base += base_encode(group)
    return base
    

def hexdecode(hinp):
    return 0


def hex2base(inp):
    bite = bytes.fromhex(inp)
    base = ''
    for i in range(0, len(bite), 3):
        base += bytes2base(bite[i:i+3])
    last = bite[len(bite) - 1]
    
    if (len(bite) % 3 == 1):
        imp = (last & 0x3) << 4
        base += base_encode(imp)
        base += '=='
    if (len(bite) % 3 == 2):
        imp = (last & 0x3F) << 2
        base += base_encode(imp)
        base += '='
        
    return base


base_dict = {
            0 : 'A',
            1 : 'B',
            2 : 'C',
            3 : 'D',
            4 : 'E',
            5 : 'F',
            6 : 'G',
            7 : 'H',
            8 : 'I',
            9 : 'J',
            10 : 'K',
            11 : 'L',
            12 : 'M',
            13 : 'N',
            14 : 'O',
            15 : 'P',
            16 : 'Q',
            17 : 'R',
            18 : 'S',
            19 : 'T',
            20 : 'U',
            21 : 'V',
            22 : 'W',
            23 : 'X',
            24 : 'Y',
            25 : 'Z',
            26 : 'a',
            27 : 'b',
            28 : 'c',
            29 : 'd',
            30 : 'e',
            31 : 'f',
            32 : 'g',
            33 : 'h',
            34 : 'i',
            35 : 'j',
            36 : 'k',
            37 : 'l',
            38 : 'm',
            39 : 'n',
            40 : 'o',
            41 : 'p',
            42 : 'q',
            43 : 'r',
            44 : 's',
            45 : 't',
            46 : 'u',
            47 : 'v',
            48 : 'w',
            49 : 'x',
            50 : 'y',
            51 : 'z',
            52 : '0',
            53 : '1',
            54 : '2',
            55 : '3',
            56 : '4',
            57 : '5',
            58 : '6',
            59 : '7',
            60 : '8',
            61 : '9',
            62 : '+',
            63 : '/'
            }

def base_encode(x):
    return base_dict[x]