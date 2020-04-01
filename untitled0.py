# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:28:00 2020

@author: Vishal
"""
list1=[]
n = int(input())
for i in range(0,n):
    x=int(input())
    list1.append(x)
y=max(list1)
list1.remove(y)
print(max(list1))