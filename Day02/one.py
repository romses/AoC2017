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
         num = int(t)
         if num>max:
            max=num
         if num<min:
            min=num

      sum = sum + (max-min)
print("Checksum = "+str(sum))
