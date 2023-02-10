# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:44:43 2022

@author: Con67
"""

#Opening the dataset
data = open("RSA-encrypted-1.txt", "r")
contents = data.read().splitlines()

#Preprocessing data, transforming each value to an integer
contents = [ int(x) for x in contents ]

#Modular exponentiation function
#Changes ascii of each codeword to binomial
#Uses binomial codeword to exponentiate 
def modexp(e,m,n):
    bn = bin(e)[3:]
    x=[0]*(len(bn)+1)
    x[0]=m
    for i in range(len(bn)):
   
        if bn[i] == '0':
            x[i+1] = (x[i]**2) %n
        if bn[i] == '1' :
            x[i+1] = (m*(x[i]**2))%n
    return(x[-1])

#Decryption function which takes the code and using private key and modular exponentiation returns message 
#Each codeword is decrypted and joined as a character
def decrypt(message2,d,n):
    asci2=[0]*(len(message2))
    word2=[0]*(len(message2))
    for i in range(len(message2)):
        asci2[i]=modexp(d,message2[i],n)
        word2[i]=chr(asci2[i])
    return(''.join(word2))

#d (private key) calculated as 20449 and n equals 99
print(decrypt(contents,20449,99157))