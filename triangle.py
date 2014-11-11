# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 08:53:41 2014

@author: Rebecca
"""

size = 45
ListA = [0]*size
ListA[0] = 0
ListA[size-1] = 0
ListA[(size-1)/2] = 1


def update(List):
    n = len(List)
    newList = [0]*n
    newList[0]=0
    newList[n-1]=0
    for i in range(1,n-1):
        newList[i] = List[i-1]^List[i+1]
    return newList

def P(List):
    print ''
    for each in List:
        if each == 1:
            print"#",
        elif each == 0:
            print " ",

for i in range(0,size):
    P(ListA)
    ListA = update(ListA)
    
