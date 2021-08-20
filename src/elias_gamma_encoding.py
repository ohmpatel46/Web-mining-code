# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:16:47 2021

@author: ohmpa
"""

from math import log
  
log2 = lambda x: log(x, 2)
  
def Unary(x):
    return (x-1)*'0'+'1'
  
def Binary(x, l = 1):
    s = '{0:0%db}' % l
    return s.format(x)
      
def Elias_Gamma(x):
    if(x == 0): 
        return '0'
  
    n = 1 + int(log2(x))
    b = x - 2**(int(log2(x)))
  
    l = int(log2(x))
  
    return Unary(n) + Binary(b, l)
n=int(input("Enter the number to be encoded: "))
      
print(Elias_Gamma(n))