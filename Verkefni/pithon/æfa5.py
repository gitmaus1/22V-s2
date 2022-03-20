from dataclasses import replace
from random import*
from tkinter import END
from math import*


##########################################################################valmind
teljary=0
svar = "já"
while svar == "já" or svar == "Já":
    teljary += 1
    print("Sláðu inn 1 til að :")
    print("Sláðu inn 2 til að :")
    print("Sláðu inn 3 til að stöðva keyrslu forrits:")
    val = int(input(": "))

    if(val==1):
     print("valdir 1")
    elif(val==2):
     print("valdir 2")
    elif(val==3):  
     svar = "nei"
    else:
     print("willa") 
print("valmyndin var keyrð",teljary)
#############################################################################
das=int(input("Hversu oft viltu sjá orðið woohoo:"))

for x in range(das+1):
    print(x*"woohoo - ")

for i in range(50,0,-2):#tala1 er birjunartala tala2 er lokatala tala3 stjórnar breitingu getur verið + eða -
    print(i)#ef það er bara gefin 1 tala þá er það altaf frá 0 up í
print("bill")
for i in range(10):#ef það er bara gefin 1 tala þá er það altaf frá 0 up í
    print(i)
print("margföldunar tafla")
for i in range(11):#range gerir up að þanig til að fá 10 þartu að skrifa 11
    print(i*8, end=" ")#end=" " 

##########################################################################
aldur= int(input("fæðingaræár: "))

if aldur % 2 == 0:
    print("slet tala og þú ert",2022-aldur)
else:
    print("ódatala og þú ert",2022-aldur)


for tala in range(1,21):
    if tala % 3 == 0:
        print(tala," er í 3 sinnum töflunni")
    else:
        print(tala," er ekki í 3 sinnum töflunni")

##############################################################################
print(sqrt(100))
print(pow(2,3))