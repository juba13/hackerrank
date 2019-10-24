#!/bin/python3

import sys

def nthFebo(n) :
    if n==1 and n==2:
        return 1
    elif n==3:
        return 2
    else :
        return  int(round((1.61803398875**n)/(5**(1/2))))

if __name__ == '__main__':
    t = int(input().strip())
    for a in range(t):
        sum=2
        n = int(input().strip())
        for i  in range(6,n+1,3):
               sum+=nthFebo(i)
               print(sum)

    
          
