# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:43:22 2021

@author: 47483
"""
# =============================================================================
# Convert the int to binary (Remove first two characters replace('0b',''))
# Convert the binary to string
# Remove the starting and trailing  0 
# Split with 1 from the string to find the subsequences of strings
# Find the length of the longest substring
# =============================================================================

def solution(N):
    bnr = bin(N). replace('0b','')
    bns=str(bnr)
    bnl=bns.strip('0')
    bnsplit=bnl.split('1')
    gap=max(bnsplit)
    mgap=len(gap)
    return  mgap

N=529
print(solution(N))