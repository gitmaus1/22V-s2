from ast import Num
from dataclasses import replace
from itertools import count
from os import sep
from random import*
from tarfile import LENGTH_LINK
from tkinter import END, SW, W
from math import*
from random import randint
import random
from collections import Counter
import collections
from dataclasses import replace
from unicodedata import digit
import math
import re



teljary=0
svar = "já"
while svar == "já" or svar == "Já":
    teljary += 1
    print("Sláðu inn 1 fyrir Slembilisti:: 2 Gengur upp í 7 og 3:: 3 fyrir Orðlisti 4 fyrir Eins ")
    print("Sláðu inn 5 til að stöðva keyrslu forrits:")
    val = int(input(": "))
    print("valdir ",val)

    if(val==1):






##################################################################################1
        for s in range(100,401):
            if s %2==0:
                print(s,end=(":"))


        ##################################################################################2
    if(val==2):

        listi1=[]


        tall=0


        listi2=[]

        listi3=[]

        for s in range(100):
            tenningar1=randint(200,301)
            listi1.append(tenningar1)
            if tenningar1==251:
                tall+=1
            if tenningar1> 250:
                listi2.append(tenningar1)
            if tenningar1 %3==0 :
                if tenningar1  %5!=0:
                    listi3.append(tenningar1)
        summa=sum(listi1)

        print("listi2",listi1)

        print("suma er: ","{:.1f}".format(summa))

        print("251 kemur fyrir: ",tall)

        print("listi2",listi2)

        print("listi3",listi3)


        ##################################################################################3

    if(val==3):
        val3=input("val3: ")


        #int4 = int("".join(filter(str.isdigit, val3)))
        #print(int4)

        h=0

        talaaa=0
        # þeta verkefni er martröð ég 
        sum_digit = 0
        for x in val3:
            if x.isdigit():
                sum_digit += int(x)
            if x == "h":
                h+=1
            if x.isdigit():
                talaaa+=1

        print("það eru svona mörg h: ",h)
        print("það eru svona mörar tölur: ",talaaa)


        print("Summa talna er : ", sum_digit)

        res1 = re.sub(r'[A-m]', '#', val3) 
        res2 = re.sub(r'["0-9"]', "#", res1)
        res3 = re.sub(r'["a-m "]', "#", res2)
        res4 = re.sub(r'["o-z "]', "#", res3)
        res4 = re.sub(r'["O-Z "]', "#", res3)

        res4 = re.sub(r'["qQwWrRtTyYuUoOpPðÐæsSzZxXvVþÞÆæ"]', "#", res3)

        res5 = re.sub(r'["!"#$%&/()=Ö_*?ÐPÆÞ:;>"]', "#", res4)

        #qQwWrRtTyYuUoOpPðÐæsSzZxXvVnNþÞ
        #utcoma=res1+res2

        print(res4)

        input()



    elif(val==4):  
     svar = "nei"
    else:
     print("willa") 
print("valmyndin var keyrð",teljary)



