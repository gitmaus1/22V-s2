from dataclasses import replace
from random import*
from tkinter import END
from math import*





nafmn=input("nafn: ")
dt=len(nafmn)
while dt>0: 
    sa=nafmn[0:dt] 
    print(sa)
    dt-=1
print("end")


##################################################
print(sqrt(100))
print(pow(2,3))
print(min(2,10))
print(max(2,10))
print(factorial(4))#4*3*2*1
print(abs(-123))
print(randint(1,100))
print(randrange(20,30))#randrange prentar ekki síðustu tölu

for i in range(5,1000,10):
    print(i)
for i in range(20,300):
    print(i)

dddd=int(input("0 til 9: "))
dassss=int(input("0 til 9: "))
kaaaaa="abcdefghjk"
print(kaaaaa[dddd:dassss])


kaaaaa="abcdefghjk"
print(kaaaaa[-2:])
print(kaaaaa.lower())
print(kaaaaa.upper())

##########################################################################################


teljary=0
svar = "já"
while svar == "já" or svar == "Já":
    teljary += 1
    print("Sláðu inn 1 til að gefa kenitöllu:")
    
    print("Sláðu inn 2 til að stöðva keyrslu forrits:")
    val = int(input(": "))

    if(val==1):
     print("valdir 1")
     kt=input("kenitala eingin - ne bill: ")
     if( len(kt) == 10) or int(kt[0:2]) <= 31 and int(kt[2:4]) <= 12 :
         print("kt ok")
         print(" amæli þit er",kt[0:2],":",kt[2:4])
     else:
        print("error")
 
    elif(val==2):  
     svar = "nei"
    else:
     print("willa") 
print("valmyndin var keyrð",teljary)



tart=input("text: ")
tart2=tart[0:2] + tart[-2:]
print(tart2)

nafmn=input("nafn: ")
dt=len(nafmn)
while dt>0: 
    sa=nafmn[0:dt] 
    print(sa)
    dt-=1
print("end")