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


#list1 = [1, 2, 3]
#list2 = [3, 2, 4]
#def multiplyList(myList) :
     
    # Multiply elements one by one
#    result = 1
#    for x in myList:
#         result = result * x
#    return result
     
# Driver code

#print(multiplyList(list1))
#print(multiplyList(list2))
def margfalta(marglist) :
     
    # margfalda
    sumaner = 1
    for d in marglist:
         sumaner = sumaner * d
    
    return sumaner

#print(margfalta(list1))
print(margfalta(daft))
print("tölur undir 15: ",daft," og suman er: ",margfalta(daft),sep)
print(snort)
















print("næst hæsta tala er: ", snort[-2])
print("minstu 5 tölur eru : ", snort[0],snort[1],snort[2],snort[3],snort[4])

#dum=
#print(dum)

sum=0
for k in range(0, len(snort)):
    sum = sum + snort[k]
print("suma er ",sum)
x = len(snort)
print("listin er ",x," langur")







tort=[random.randint(0,100) for h in range(20)]
print(tort)
start=[]
start.append(tort[0])
start.append(tort[-1])
print(start)


##################################################################################
#2
##################################################################################
#3
##################################################################################
#4