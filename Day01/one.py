#!/usr/bin/python

last=""
cur=""
sum=0

with open("input") as f:
   for line in f:
      line=line.strip('\n')
      line=line+line[:1]

      for ch in line:
         cur = ch
         if(cur == last):
            sum=sum+int(cur)
         last = cur

print("The captcha-code is :"+str(sum))
