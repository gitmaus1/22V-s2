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
#exp



svar3listi = []

for a in range(5):
    orð1 = input("Sláðu inn orð: ")
    svar3listi.append(orð1)

book= input("Fyrsti stafur sem þú villt eyða orðum úr lista: ")
print(svar3listi)
for i in svar3listi:
    if book == i[0]:
        print("rétt")



##################################
##svar2listi = []

##def suman(sumlist) :
     
    # margfalda
##    ser = 0
##    for n in sumlist:
##         ser = ser + n
    
##    return ser






##for n in range(4000,8201):
##    if n % 7 == 0 or n % 3 == 0:
##        svar2listi.append(n)





##siffer=0
##for n in svar2listi:
##    print(n, end=",,, ")
##    siffer+=1
##    if siffer==1:
##        print("\n")
##        siffer=0

#safffaren=len(svar2listi)
##def meðal(meðallist) :
     
    # margfalda
##    ssser = 0
##    for n in meðallist:
##         ssser = (ssser + n)
##    avg = ssser / len(svar2listi)
##    return avg

##print("suman er: ",suman(svar2listi))
##print(sum(svar2listi))
##skan= meðal(svar2listi)

##print("meðal er: ","{:.2f}".format(skan))

#print("  meðal er: ")

#print(meðal(svar2listi))

##print(len(svar2listi))
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
    if siff==15:
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

svar2listi = []

def suman(sumlist) :
     
    # margfalda
    ser = 0
    for n in sumlist:
         ser = ser + n
    
    return ser






for n in range(4000,8201):
    if n % 7 == 0 or n % 3 == 0:
        svar2listi.append(n)





siffer=0
for n in svar2listi:
    print(n, end=",,, ")
    siffer+=1
    if siffer==1:
        print("\n")
        siffer=0

#safffaren=len(svar2listi)
def meðal(meðallist) :
     
    # margfalda
    ssser = 0
    for n in meðallist:
         ssser = (ssser + n)
    avg = ssser / len(svar2listi)
    return avg

print("suman er: ",suman(svar2listi))
print(sum(svar2listi))
skan= meðal(svar2listi)

print("meðal er: ","{:.2f}".format(skan))

#print("  meðal er: ")

#print(meðal(svar2listi))

print(len(svar2listi))


##################################################################################
#3
##################################################################################
#4