from dataclasses import replace
from random import*
from tkinter import END
from math import*
from random import randint
import random





thislist = []
jes="Jes"
while jes=="Jes":
    
    texter= input("matarlisti: ")


    thislist.append(texter)

   
    print("1 til að bæta við 2 til að hæta")
    bæ=input("")
    if bæ=="1":
        print("waldir 1")
    elif bæ=="2":
        jes="no"
    else:
        print("error")
sort= sorted(thislist)
print(sort)



soft=[random.randint(0,10) for i in range(15)]

snort= sorted(soft)

print(snort)

print("Largest element is:", snort[-1])
print("Smalest element is:", snort[0])
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
