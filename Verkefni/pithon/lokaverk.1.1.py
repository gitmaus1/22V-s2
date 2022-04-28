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
#exp í exp eru tilraunir til að leisa verkefnin oft án comenta

#################################

control="ja"
suma=1
ass=0
while control == "ja":

    talapart2=int(input("Sláðu inn tölu: "))
    if talapart2==0:
        control="stop"

    for i in range(talapart2):
        
        ass=suma*i
        
        suma+=1
        
        das=ass*(i+suma)
            
        print(ass*suma)

#################################
#farðegar=int(input("Hvað eru margir skráðir í ferðina?: "))

#fjöldibíla=0
#if farðegar >= 5:

#    print("skráðir farðegar",farðegar)
#    while farðegar >= 5:
#        fjöldibíla+=1
#        farðegar-=5
#    print("Fjöldi bíla sem þarf: ",fjöldibíla)
#    print("Fjöldi í síðasta bílnum: ",farðegar)

#else:
#    print("Því miður eru ekki nógu margir skráðir, hætt er við ferðina.")
################################

##################################################################################
##Liður 1 – Bílar

#fillgist með fjölda farðega
farðegar=int(input("Hvað eru margir skráðir í ferðina?: "))
#fillgist með fjölda bíla
fjöldibíla=0
#chekar kvort það eru nógu margir farðegar
if farðegar >= 5:
    #útkoma
    print("skráðir farðegar",farðegar)
    if farðegar %5!=0:
        fjöldibíla+=1
        


    #reiknar útcomu
    while farðegar >= 5:
        fjöldibíla+=1
        farðegar-=5
    #meiri útcomur
    print("Fjöldi bíla sem þarf: ",fjöldibíla)
    print("Fjöldi í síðasta bílnum: ",farðegar)
#ef ekki nógu margir
else:
    print("Því miður eru ekki nógu margir skráðir, hætt er við ferðina.")

##################################################################################
##Liður 2 – Margföldunarruna


##################################################################################
##Liður 3 – Snaran


##################################################################################
##Liður 4 – Texti


##################################################################################
##Liður 5 – Marföldun almennra brota


##################################################################################
##Liður 6 – Teningaspilið Craps


##################################################################################
##Liður 7 – Þyngdarstuðull:


##################################################################################
##Liður 8 – Teningar


