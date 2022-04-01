from ast import Num
from dataclasses import replace
from itertools import count
from random import*
from tkinter import END, SW
from math import*
from random import randint
import random
from collections import Counter
import collections
from dataclasses import replace
from unicodedata import digit



#str = input()
   
 
#print ("Original string: " + str) 
   
# Removing char at pos 3 
# using slice + concatenation 
#res_str = str[:0] +  str[1:] 
   
 
#print ("String after removal of character: " + res_str) 




#svar4=input("svar4: ")
#stem=0
#daft=len(svar4)
#print(len(svar4))
#print(svar4)
#while 0 <= daft:
#    nuna=svar4[:-0] + svar4[:stem]
#    print(nuna)
#    stem-=1
#    daft-=1
#print(nuna)



#for i in range(len(svar4)):
#    defp=i-1
#    print(i)
#    svar4.pop(0)
#    print(svar4)


#print(svar4)




#svar4=[input("svar4: ")]

#for i in range(len(svar4)):
#    defp=i-1
#    print(i)
#    svar4.pop(0)
#    print(svar4)


#print(svar4)



#######################################################################
#1
svar1=input("svar1: ")
#svor1=print(Counter(svar1))
print(Counter(svar1))
svor=count()


#results = collections.Counter(svar1)
#print(results)
#######################################################################
#2
def aframback(s):
    return s == s[::-1]
 
  

s = input("svar2: ")
ans = aframback(s)
 
if ans:
    print(s," er samhverfur strengur")
else:
    print(s," er ekki samhverfur strengur")


#######################################################################
#3

svar3=input("svar3: ")
svar32=input("svar3: ")
if len(svar3) >= 5 and len(svar32) >= 5:

      stuff=svar3[:2]+svar32[:-2]
      print(stuff)
      ruff=stuff.upper()
      print(ruff)
      duff=stuff.lower()
      print(duff)
      print(len(stuff))
else:
      print("error")
      



#######################################################################
#4
svar4=input("svar4: ")
stem=0
daft=len(svar4)
#print(len(svar4))
print(svar4)
while 0 <= daft:
    nuna=svar4[:-0] + svar4[:stem]
    print(nuna)
    stem-=1
    daft-=1
#######################################################################
#5
svar5=input("svar5: ")
svor5=svar5.swapcase() 
swore5=svor5.replace("1", "#") 
swore52=swore5.replace("2", "#") 
swore53=swore52.replace("3", "#") 
swore54=swore53.replace("4", "#") 
swore55=swore54.replace("5", "#") 
swore56=swore55.replace("6", "#") 
swore57=swore56.replace("7", "#") 
swore58=swore57.replace("8", "#") 
swore59=swore58.replace("9", "#") 

print(swore59)
#######################################################################
#6
#######################################################################