#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 00:58:47 2023

@author: sefat07
"""

def rec_sum(n):
    if n == 1:
        return 1
    else:
        return n + rec_sum(n-1)

def rec_fac(n):
    if n == 1:
        return 1
    else:
        return n * rec_fac(n-1)

def fac(n):
    sum = 1
    for i in range(n, 1, -1):
        sum = sum * i
    return sum
    
    
def sum_int(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_int(n // 10)
    
def sum_int(n):
    summ = 0
    while n % 10 != 0:
        summ = summ + n % 10
        n = n // 10
    summ = summ + n
    return summ

word = 'ilovedogsjohn'
word_list = ['i', 'am', 'love', 'dogs', 'john']

def word_split(word, word_list):
    i = 1
    start = 0
    out = []
    while i <= len(word):
        if word[start:i] in word_list:
            out.append(word[start:i]) 
            start = i
            i += 1
        else:
            i += 1      
    return out
    
s = 'know'

def rever_str(s):
    if len(s) == 1:
        return s[-1]
    else:
        return s[-1] + rever_str(s[:-1])

#%%%%%%%%%%%%%%
num = 4376

def rever_int(num):
    rev = []
    while num > 0:
        rev.append(num%10)
        num = num//10
    
    summ = 0
    i = 0
    while i < len(rev):
        summ += rev[i] * 10**(len(rev) - i - 1)
        i += 1
    return summ  

#%%%%%%%%%

def permute(s):
    
    out = []
    if len(s) == 1:
        return s[0]
    for idx, i in enumerate(s):
        for j in permute(s[:idx] + s[idx+1:]):
            out.append(i+j)
    
    return out
    
#%%%%%%%%

def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    

def fib_dyn(num):
    out = {}
    if num == 0 or num == 1:
        return num
    else:
        out[num] = fib_dyn(num-1) + fib_dyn(num-2)
    return out[num]

out = [None] * 101   
def fib_dyn(num):

    if num == 0 or num == 1:
        return num
    if out[num] != None:
        return out[num]
    else:
        out[num] = fib_dyn(num-1) + fib_dyn(num-2)
    return out[num]   

####

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
fib_dict = {}
def fib(n):
    if n == 0 or n == 1:
        return n
    if n not in fib_dict.keys():
        fib_dict[n] = fib(n-1) + fib(n-2)
    return fib_dict[n]
    
#%%%%%%%%%%%%%%%%%   label  correcting (shortest path) %%%%%%%%%

n = 74
coin = [1, 5, 10, 25]

n = 10
coin = [1, 5, 10]

min_coin = 10**5

c, d_star, d = {}, {}, {}
c[0], d_star[0], d[0] = {}, {}, {}
for i in coin:
    c[0][i] = i
    d[0][i] = 1
    if c[0][i] == n:
        min_coin = d[0][i]
        print(d[0][i])
    d_star[0][i] = d[0][i]


#####
k = 1
while k < n:
    c[k], d[k] = {}, {}
    for i in c[k-1].keys():
        for j in coin:
            if c[k-1][i] < n and d[k-1][i] < min_coin:
                c[k][i,j] = c[k-1][i] + j
                d[k][i,j] = d[k-1][i] + 1
                if c[k][i,j] == n and d[k][i,j] < min_coin:
                    min_coin = d[k][i,j]
                    print(i,j)
    if c[k] == {}:
        break
    k += 1
#####

################### dynamic programming ###########

num = 10    # state: residual to reach the num   #control: coins to pick
coins = [1,2,3,10]
picks = {}
#picks[0] = 0    #picks[i,j] = state i , control j 

for i in range(1, num+1, 1):
    for j in coins:
        if i - j <= num:
            if i - j == 0:
                picks[i,j] = 1 + 0 #picks[i-j]
            else:
                try:
                    picks[i,j] = 1 + min([picks[(k,l)] for (k,l) in picks.keys() if k==i-j])
                except:
                    pass

out = min([picks[(k,l)] for (k,l) in picks.keys() if k==num])

# (10,3) --> (7,3) --> (4,3) -->(1,1)


num = 74
coins = [1,5,10, 25]




