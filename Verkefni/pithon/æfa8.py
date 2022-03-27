from dataclasses import replace
from random import*
from tkinter import END
from math import*
from random import randint
import random


listmist=[]

daft=random.randint(5,25)


soft=daft*10


listmist.append(soft)

print(listmist)



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


