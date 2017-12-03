#!/usr/bin/python

import sys

sum=0

with open("input") as f:
   for line in f:
      line=line.strip('\n')
      tokens=line.split('\t')

      max=0
      min=10000000000
      for t in tokens:
         t=float(t)
         for u in tokens:
            u=float(u)
            if(t!=u):
               if (u/t)==int(u/t):
                  sum = sum + (u/t)
               if (t/u)==int(t/u):
                  sum = sum + (t/u)
print("The new correct checksum is " + str(sum/2))
