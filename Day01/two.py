#!/usr/bin/python

last=""
cur=""
sum=0

with open("input") as f:
   for line in f:
      line=line.strip('\n')
      line=line+line
      length=int(len(line)/2)

      for i in range(0,length):
         if line[i:i+1]==line[i+int(length/2):i+int(length/2)+1]:
            sum=sum+int(line[i:i+1])
print("The new captcha-code is :"+str(sum))
