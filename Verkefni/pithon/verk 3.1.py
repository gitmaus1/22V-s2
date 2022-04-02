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

#test_string = 'This is a test!'
#print (test_string [1:-1])

#dem=0
#stemm=0
#svar6=input("svar6: ")
#daftt=len(svar6)
#print(svar6)
#while 0 <= daftt:
    
    
    #daftt-=1

   # print (svar6 [dem:stemm])
  #  dem+=1
 #   stemm-=1














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
dem=0
stemm=0
svar6=input("svar6: ")
daftt=len(svar6)
print(svar6)
while 0 <= daftt:
    daftt-=1
    print (svar6 [dem:stemm])
    dem+=1
    stemm-=1
#######################################################################
teljary=0
svar = "já"
while svar == "já" or svar == "Já":
    teljary += 1
    print("Sláðu inn 1 fyrir verk1 2 fyrir verk2 3 fyrir verk3 4 fyrir verk4 5 fyrir verk5 6 fyrir verk6:")
    print("Sláðu inn 7 til að stöðva keyrslu forrits:")
    val = int(input(": "))
    print("valdir ",val)

    if(val==1):
        svar1=input("svar1: ")
        print(Counter(svar1))
        svor=count()
    elif(val==2):
        def aframback(s):
            return s == s[::-1]
        s = input("svar2: ")
        ans = aframback(s)  
        if ans:
            print(s," er samhverfur strengur")
        else:
            print(s," er ekki samhverfur strengur")
    elif(val==3):
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
    elif(val==4):
        svar4=input("svar4: ")
        stem=0
        daft=len(svar4)
        print(svar4)
        while 0 <= daft:
            nuna=svar4[:-0] + svar4[:stem]
            print(nuna)
            stem-=1
            daft-=1
    elif(val==5):
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
    elif(val==6):
        dem=0
        stemm=0
        svar6=input("svar6: ")
        daftt=len(svar6)
        print(svar6)
        while 0 <= daftt:
            daftt-=1
            print (svar6 [dem:stemm])
            dem+=1
            stemm-=1
    elif(val==7):  
     svar = "nei"
    else:
     print("willa") 
print("valmyndin var keyrð",teljary)