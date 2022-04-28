import os

with open('india.txt','r') as f:
      f_contents=f.read()
      splitedType=f_contents.split()
      count=0
      for i in splitedType:
          if i=='india'or i=='India':
              count+=1
      print(count)
