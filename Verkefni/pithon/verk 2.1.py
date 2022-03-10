
from random import*
from tkinter import END
##########################################################################################################
#exp

#dur= int(input("tala:"))

#if dur % 2 == 0:
#          print("slet tala ")
#else:
#          print("odatala ")





svar = "já"
while svar == "já" or svar == "Já":
    print("Sláðu inn 1 til að reikna summu og meðaltal:")
    print("Sláðu inn 2 til að jöfntala eða oddatala:")
   # print("Sláðu inn 3 til að reikna ummál hrings:")
    print("Sláðu inn 3 til að stöðva keyrslu forrits:")
    val = int(input(": "))

    if val == 1:
        print("Þú gefur mér 10 tölur")
        za1 = int(input("Sláðu inn 1 tölu: "))
        za2 = int(input("Sláðu inn 2 tölu: "))
        za3 = int(input("Sláðu inn 3 tölu: "))
        za4 = int(input("Sláðu inn 4 tölu: "))
        za5 = int(input("Sláðu inn 5 tölu: "))
        za6 = int(input("Sláðu inn 6 tölu: "))
        za7 = int(input("Sláðu inn 7 tölu: "))
        za8 = int(input("Sláðu inn 8 tölu: "))
        za9 = int(input("Sláðu inn 9 tölu: "))
        za10 = int(input("Sláðu inn 10 tölu: "))
        print("summa:",(za1+za2+za3+za4+za5+za6+za7+za8+za9+za10))
        print("meðaltal:",(za1+za2+za3+za4+za5+za6+za7+za8+za9+za10)/2)
    elif val == 2:
        dur= int(input("tala:"))

        if dur % 2 == 0:
          print("slet tala ")
        else:
          print("odatala ")
    #if val == 3:
    #    print("Þú ætlar að reikna ummál hrings.")
    #    radius = int(input("Sláðu inn radíus hringins: "))
    #    print("Ummálið er: ", 2*radius*3.14)
    elif val == 3:
        for d in range(11):
         print(d*"Ég er ekki forritari")
         svar = "nei"
    else:
     print("willa") 
        
    

    




#aldur= int(input("tala:"))

#if aldur % 2 == 0:
#    print("slet tala og þú ert")
#else:
#    print("ódatala og þú ert")















#das=int(input("Hversu oft viltu sjá orðið woohoo:"))

#for x in range(das+1):
#    print(x*"woohoo - ")


#tallllla = int(input("Sláðu inn tölu: "))
#margf=1
#for x in range(tallllla,0,-1):
#    margf= margf * x
#    print(x, end=" * ")
#print(margf)



#tallllla = int(input("Sláðu inn tölu: "))
#svar=0
#teljari = tallllla
#while tallllla>0:
    
    
    #print(svar)
    
    #if teljari == 0:
    #    print("end")
 #   for t in range(tallllla):
     #   svar = tallllla * (tallllla-1)
     #   print(tallllla*tallllla)    
       # if tallllla == 0:
        # print("end")
    #elif teljari>= 0:
     #   teljari=tallllla-1 
     #   print(teljari)
     #   for t in range(teljari-1):
    #        print(svar)
        #teljari - 1
        #teljari = tallllla - 1
        #print(svar)
    #print(svar)
    #teljari = tallllla - 1
#print(svar)



#das=int(input("Hversu oft viltu sjá orðið woohoo:"))

#for x in range(das+1):
#    print(x*"woohoo - ")

#tala = int(input("Sláðu inn tölu: "))
#svar = 0
#teljari = 0
#while teljari < 0:
#    svar = svar * tala
#    teljari = teljari + 1

#print(svar)


















#trrrr=int(input("tala"))


#if trrrr <= 0:
#        print("no")
#elif trrrr >= 10:
#        print("noo")
#elif trrrr >= 0:
#        print("!")
#        print(trrrr,"*1=",trrrr*1)
#        print(trrrr,"*2=",trrrr*2)
#        print(trrrr,"*3=",trrrr*3)
#        print(trrrr,"*4=",trrrr*4)
#        print(trrrr,"*5=",trrrr*5)
#        print(trrrr,"*6=",trrrr*6)
#        print(trrrr,"*7=",trrrr*7)
#        print(trrrr,"*8=",trrrr*8)
#        print(trrrr,"*9=",trrrr*9)
#        print(trrrr,"*10=",trrrr*10)













#tasman= int(input("giska á tölu"))

#dababa=randint(1,10)
#while tasman > dababa or tasman < dababa:
#   if tasman == dababa:
#    print("til hamingju þetta er rétta talan")
     
#   elif tasman >= dababa:
#    print("talan er of há")
#    tasman= int(input("giska á tölu"))
#    dababa=randint(1,10)
#    if tasman == dababa:
#     print("til hamingju þetta er rétta talan")
#   elif tasman <= dababa:
#    print("talan er of lá")
#    tasman= int(input("giska á tölu"))
#    dababa=randint(1,10)
#    if tasman == dababa:
#     print("til hamingju þetta er rétta talan")
   







#print(randrange(20,30))#randrange prentar ekki síðustu tölu

#for i in range(5,1000,10):
#    print(i)
#for i in range(20,300):
#    print(i)

##########################################################################################################
#svar 1

talala=int(input("tala1:"))
dalalala=int(input("tala2:"))
suma = 0
for i in range(talala,dalalala):
    print(i,end="")
    suma = suma + i
if talala==dalalala or dalalala==talala + 1 or talala>dalalala:
    print("villa")
###############################################################
#elif dalalala==talala + 1:
#    print("villla")
#elif talala>dalalala:
#    print("villur")
###############################################################
print (": summan",suma)
############################################################################################################
#svar 2
das=int(input("Hversu oft viltu sjá orðið woohoo:"))

for x in range(das+1):
    print(x*"woohoo - ")
############################################################################################################
#svar 3
tasman= int(input("giska á tölu"))

dababa=randint(1,100)
while tasman > dababa or tasman < dababa:
   if tasman == dababa:
    print("til hamingju þetta er rétta talan")
     
   elif tasman >= dababa:
    print("talan er of há")
    tasman= int(input("giska á tölu"))
    dababa=randint(1,100)
    if tasman == dababa:
     print("til hamingju þetta er rétta talan")
   elif tasman <= dababa:
    print("talan er of lá")
    tasman= int(input("giska á tölu"))
    dababa=randint(1,100)
    if tasman == dababa:
     print("til hamingju þetta er rétta talan")
   




############################################################################################################
#svar 4


trrrr=int(input("tala"))


if trrrr <= 0:
        print("no")
elif trrrr >= 10:
        print("noo")
elif trrrr >= 0:
        print("!")
        print(trrrr,"*1=",trrrr*1)
        print(trrrr,"*2=",trrrr*2)
        print(trrrr,"*3=",trrrr*3)
        print(trrrr,"*4=",trrrr*4)
        print(trrrr,"*5=",trrrr*5)
        print(trrrr,"*6=",trrrr*6)
        print(trrrr,"*7=",trrrr*7)
        print(trrrr,"*8=",trrrr*8)
        print(trrrr,"*9=",trrrr*9)
        print(trrrr,"*10=",trrrr*10)








#trrrr=int(input("tala"))
#while trrrr > 10 or trrrr < 0:
#    if trrrr <= 0:
#        print("no")
#    elif trrrr >= 10:
#        print("noo")
#    else:
#        print(trrrr*1)
#        print(trrrr*2)
#        print(trrrr*3)
#        print(trrrr*4)
#        print(trrrr*5)


############################################################################################################
#svar 5
tallllla = int(input("Sláðu inn tölu: "))
margf=1
for x in range(tallllla,0,-1):
    margf= margf * x
    print(x, end=" * ")
print("=",margf)


############################################################################################################
#svar 6

