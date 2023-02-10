# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:49:00 2022

@author: Con67
"""

#Factorisation
#Choose a=281 since this is prime and gcd(281,99157)=1
#Factorisation to find period r and x, where gcd(x+-1,n) = p and q
i=1
while True:
     i=i+1
     a= (281**i)%99157
     if a==281:
         r=i-1
         x = 281**(int(r/2))%99157
         print(r)
         print(x)
         break


