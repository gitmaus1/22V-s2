from ast import Num
from dataclasses import replace
from itertools import count
from os import sep
from random import*
from tkinter import END, SW
from math import*
from random import randint
import random
from collections import Counter
import collections
from dataclasses import replace
from unicodedata import digit
import math
##################################################################################
#1

soft=[]
daft=[]
sep = 0
for i in range(150):
    tala = random.randint(4,84)
    ska = soft.append(tala)
    if tala < 15:
         daft.append(tala)
         
     
         

snort= sorted(soft)



def margfalta(marglist) :
     
    # margfalda
    sumaner = 1
    for d in marglist:
         sumaner = sumaner * d
    
    return sumaner

print("tölur undir 15: ")
for n in daft:
    print(n, end="; ")


print(" og sinnum er: ",margfalta(daft))
#print(snort)

siff=0
for n in snort:
    print(n, end="; ")
    siff+=1
    if siff==5:
        print("\n")
        siff=0
   














print("næst hæsta tala er: ", snort[-2])
print("minstu 5 tölur eru : ", snort[0],snort[1],snort[2],snort[3],"og 5 lægsta tala er",snort[4])



sum=0
for k in range(0, len(snort)):
    sum = sum + snort[k]
print("suma er ",sum)
x = len(snort)
print("listin er ",x," langur")










##################################################################################
#2
##################################################################################
#3
##################################################################################
#4