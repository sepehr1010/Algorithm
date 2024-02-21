#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 19:25:06 2024

@author: sefat07
"""
str1 = 'Crap py'
str2 = 'Ycrap p'
def anagram(str1, str2):
    str1, str2 = str1.replace(" ", '').lower(), str2.replace(" ", '').lower()
    str1_dict = {}
    for i in str1:
        if i in str1_dict:
            str1_dict[i] += 1
        else:
            str1_dict[i] = 1
    str2_dict = {}       
    for i in str2:
        if i in str2_dict:
            str2_dict[i] += 1
        else:
            str2_dict[i] = 1
    out = []      
    for i in str1_dict:
        try:
            if str1_dict[i] == str2_dict[i]:
                out.append(True)
        except:
            return False
    return all(out)
        
anagram(str1, str2)

#%%%%%%%%%%%%%%%%

def pairsum(array, value):
    out = set()
    for idx, i in enumerate(array):
        for j in array[idx+1:]:
            if i + j == value:
                out.add((i,j))
    return out

def pairsum(array, value):
    seen = set()
    out = set()
    for i in array:
        target = value - i
        if target not in seen:
            seen.add(i)
        else:
            out.add((min(i, target), max(i, target)))
    return out

pairsum([1,3,2,2, 1, 1, 2, 3], 4)

#%%%%%%%%%%%%%%%%

arr1 = [1,2,3,4,5,6,7, 7]
arr2 = [7, 5, 6, 3,4,2,1]

def diff(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return i
        else:
            arr2.remove(i)

#%%%%%%%%%%%%%%%%%5

arr = [1,2,-1,3,4,10,10,-10,-1]

def large_consum(arr):
    out = {}
    for idx, i in enumerate(arr):
        for jdx, j in enumerate(arr[idx+1:]):
            out[idx,idx+1+jdx] = sum(arr[idx:idx+1+jdx])
    index = max(out, key=out.get)
    max_sum = max(out.values())
    max_sum = max([value for key, value in out.items()])
    index = [key for key, value in out.items() if value==max_sum] 
    return index, max_sum
        
#%%%%%%%%%%%%%%%%%%%

string = ' space is here  '

def sent_rev(string):
    string2 = string.split(" ")
    i = 0
    while string2[i] == '':
        i += 1
    string3 = string2[i:]
    j = len(string3) - 1
    while string3[j] == '':
        j -= 1      
    string4 = string3[:j+1]
    
    
    
    i = 0
    start = i
    words = []
    while i < len(string):
        if string[i] == ' ':
            words.append(string[start:i])
            start = i + 1

        i += 1
    words.append(string[start:i]) 
    words = [i for i in words if i != ""]
     
    " ".join(words[::-1])
    
    
    i = len(string4) - 1
    string5 = []
    while i >= 0:
        string5.append(string4[i])
        i -= 1
    
    string5 = string4[::-1]
    
    return " ".join(string5)


#%%%%%%%%%%%%%%%%%%%%%%%%


string = 'AAABBddOppppp'

def str_comp(string):
    seen = ''
    count = 0
    i = 0
    out = ''
    while i < len(string):
        if string[i] != seen:
            if seen != '':
                out += seen + str(count)
            seen = string[i]
            count = 1
        else:
            count += 1 
        i += 1
    out += seen + str(count)
    return out
        

#%%%%%%%%%%%%%%%%%%

string = 'aabfgghft'
string = 'abfght'

def uni_char(string):
    seen = []
    i = 0
    while i < len(string):
        if string[i] not in seen:
            seen.append(string[i])
            i += 1
        else:
            return False
    return True
    
    
def uni_char(string):
    if len(set(string)) == len(string):
        return True
    else:
        return False
    
    
    
    
    
    
    
    
    














