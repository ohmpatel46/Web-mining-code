# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:04:31 2021

@author: ohmpa
"""

import math

def decode(t):
    x=[];
    if(t==0):
        return [0];
    while(t>0):
        x.append(t%2);
        t=int(t/2);
    return x

def unary(t):
    y=[];
    for i in range(t-1):
        y.append(0);
    y.append(1)
    return y;    

x=int(input('Enter a number: '))  
b=int(input('Enter value of b: '))
q=int(x/b)
y=unary(q+1)
r=x-(q*b)
i=math.floor(math.log(b,2));
d=math.pow(2,i+1)-b;
if(r>=d):
    r+=int(d);
r2=decode(r);
if(len(r2)<=i and r>=d):
    r2.append(0);
if(len(r2)<i and r<d):
    r2.append(0);    
r2=r2[::-1];
y=y+r2;
print('Code: ',y);