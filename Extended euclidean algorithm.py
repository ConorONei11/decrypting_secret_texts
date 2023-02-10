# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:31:34 2022

@author: Con67
"""
#Extended Euclidean algorithm
#Finding gcd of two intgers a and b
def gcd(a,b):
    while b>0:
      r=a%b
      a=b
      b=r
    return(a)

#Finding p and q
print(gcd(51525,99157))
print(gcd(51527,99157))
#Therefore p = 229 and q = 433 (correct since both prime)
#Now transmitted can begin to be encrypted ... ->

#Finding gcd of two integers a and b
#Also finding n and m where n*a+m*b = gcd(a,b)
#When returned, a=gcd, x1=n and y1=b
def gcd2(a,b):
    x0=0
    x1=1
    y0=1
    y1=0
    while b>0:
        q=a//b
        r=a%b
        a=b
        b=r
        x00=x1-q*x0
        x1=x0
        x0=x00
        y00=y1-q*y0
        y1=y0
        y0=y00
    return(a,x1,y1)

#Since (p-1)(q-1)=98496 and public key e = 289
print(gcd2(98496,289))

#Find that the private key d = 20449, and the message can now be decrypted (as seen on decrypted dataset file)
