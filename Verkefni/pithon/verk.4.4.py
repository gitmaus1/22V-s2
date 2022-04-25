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



##verksvar4=["bill","billibob","bobbillibob","tim","tom","björn","harry"]

##newlist = [x.lower() for x in verksvar4]

##print(newlist)

##verksvar4two=["bill","billibob","dick","sunny"]

##wlist2 = [x.capitalize() for x in verksvar4two]

##print(newlist2)




##listinumer3=[]

##listinumer4=[]



##count = 0
##for i in range(len(verksvar4)):
##        for j in range(len(verksvar4two)):
##            if verksvar4[i] == verksvar4two[j]:
##                count += 1
##                print(i,"er sama",j)
##                listinumer3.append(verksvar4[i])
##                #verksvar4.remove(i)
##                break
##            else:
##                listinumer4.append(verksvar4[i])
##                listinumer4.append(verksvar4two[j])
##print(verksvar4)
##print(listinumer3)
##print(listinumer4)
##a = list(set(listinumer4))
##print(a)
# call the function
##print(count)







##list1 = [6, 1, 5, 2, 3]
##list2 = [3, 5, 2, 1, 4]

#def compare(list1, list2):

    # Check if all the elements of both the lists are same
##count = 0
##for i in range(len(list1)):
##        for j in range(len(list2)):
##            if list1[i] == list2[j]:
##                count += 1
                
##                break
 

# call the function
##print(count)
#print(compare(list1, list2))
#print(compare(newlist, newlist2))

##input()



#svar3listi = []

#for a in range(5):
#    orð1 = input("Sláðu inn orð: ")
#    svar3listi.append(orð1)


#print("obreitur listi: ",svar3listi)
#nkjhb=sorted(svar3listi)
#print("raðað",nkjhb)

#######################
#def backvatd(x):
#  return x[::-1]
#svar3listi[0]=  backvatd(svar3listi[0])
#svar3listi[-1]=  backvatd(svar3listi[-1])
#print("nema hvað fyrsta og síðasta orðið á að skrifast út öfugt",svar3listi)
#print("nema hvað fyrsta og síðasta orðið á að skrifast út öfugt",svar3listi)
#print("nema hvað fyrsta og síðasta orðið á að skrifast út öfugt",svar3listi)
#for i in svar3listi:
#    backvatd(i[0])
#    if i[0]:
#       i[::-1]
#       print(i)
#print(svar3listi)

#######################
#print(svar3listi[0])
#nufsed1=0
#nufsed2=0
#nufsed3=0
#for i in svar3listi:
#    if len(i) == 5:
#        print(i,"er sama sem 5 og er með : ",len(i)," carectera")
 #       nufsed1+=1

#    if len(i) > 5:
#       print(i,"er  leingri en 5 og er með : ",len(i)," carectera")
#        nufsed2+=1

#    if len(i) < 5:
#        print(i,"er  stitri en 5 og er með : ",len(i)," carectera")
#        nufsed3+=1


#print("það eru : ",nufsed1," orð sama sem 5")
#print("það eru : ",nufsed2," orð leingri en 5")
#print("það eru : ",nufsed3," orð stitri en 5")
########################
#book= input("Fyrsti stafur sem þú villt eyða orðum úr lista: ")
#eitt=0

#iasdf=0
#while iasdf <  5:
# for i in svar3listi:
    #print(i)
    #if book == i[0]:
   #     eitt+=1
  #      print(i,"war fjarlægt")
 #       svar3listi.remove(i)
# iasdf+=1
  

#print(eitt,"orðum var eitt")
#print(svar3listi)
#######################

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
teljary=0
svar = "já"
while svar == "já" or svar == "Já":
    teljary += 1
    print("Sláðu inn 1 fyrir Slembilisti:: 2 Gengur upp í 7 og 3:: 3 fyrir Orðlisti 4 fyrir Eins ")
    print("Sláðu inn 5 til að stöðva keyrslu forrits:")
    val = int(input(": "))
    print("valdir ",val)

    if(val==1):
        





############################################################################################################


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
    elif(val==2):
        
    




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
            print(n, end=", ")
            siffer+=1
           # if siffer==1:
            #    print("\n")
            #    siffer=0

        #safffaren=len(svar2listi)
        def meðal(meðallist) :
            
            # margfalda
            ssser = 0
            for n in meðallist:
                ssser = (ssser + n)
            avg = ssser / len(svar2listi)
            return avg

        print("suman er: ",suman(svar2listi))
        #print(sum(svar2listi))
        skan= meðal(svar2listi)

        print("meðal er: ","{:.2f}".format(skan))

        #print("  meðal er: ")

        #print(meðal(svar2listi))

        print(len(svar2listi))


##################################################################################
#3
    elif(val==3):
        
        















        svar3listi = []

        for a in range(5):
            orð1 = input("Sláðu inn orð: ")
            svar3listi.append(orð1)


        print("obreitur listi: ",svar3listi)
        nkjhb=sorted(svar3listi)
        print("raðað",nkjhb)

        #######################
        def backvatd(x):
          return x[::-1]
        svar3listi[0]=  backvatd(svar3listi[0])
        svar3listi[-1]=  backvatd(svar3listi[-1])
        print("nema hvað fyrsta og síðasta orðið á að skrifast út öfugt",svar3listi)
        print("nema hvað fyrsta og síðasta orðið á að skrifast út öfugt",svar3listi)
        print("nema hvað fyrsta og síðasta orðið á að skrifast út öfugt",svar3listi)
        #for i in svar3listi:
        #    backvatd(i[0])
        #    if i[0]:
        #       i[::-1]
        #       print(i)
        #print(svar3listi)

        #######################
        #print(svar3listi[0])
        nufsed1=0
        nufsed2=0
        nufsed3=0
        for i in svar3listi:
            if len(i) == 5:
                print(i,"er sama sem 5 og er með : ",len(i)," carectera")
                nufsed1+=1

            if len(i) > 5:
                print(i,"er  leingri en 5 og er með : ",len(i)," carectera")
                nufsed2+=1

            if len(i) < 5:
                print(i,"er  stitri en 5 og er með : ",len(i)," carectera")
                nufsed3+=1


        print("það eru : ",nufsed1," orð sama sem 5")
        print("það eru : ",nufsed2," orð leingri en 5")
        print("það eru : ",nufsed3," orð stitri en 5")
        ########################
        book= input("Fyrsti stafur sem þú villt eyða orðum úr lista: ")
        eitt=0

        iasdf=0
        while iasdf <  5:
            for i in svar3listi:
                #print(i)
                if book == i[0]:
                    eitt+=1
                    print(i,"war fjarlægt")
                    svar3listi.remove(i)
            iasdf+=1
        

        print(eitt,"orðum var eitt")
        print(svar3listi)
        print(svar3listi)
        print(svar3listi)
        print(svar3listi)
#######################

##################################################################################
#4

    elif(val==4):
        








        verksvar4=["bill","billibob","bobbillibob","tim","tom","björn","harry"]

        newlist = [x.lower() for x in verksvar4]

        print(newlist)

        verksvar4two=["bill","billibob","dick","sunny"]

        newlist2 = [x.capitalize() for x in verksvar4two]

        print(newlist2)




        listinumer3=[]

        listinumer4=[]



        count = 0
        for i in range(len(verksvar4)):
                for j in range(len(verksvar4two)):
                    if verksvar4[i] == verksvar4two[j]:
                        count += 1
                        print(i,"er sama",j)
                        listinumer3.append(verksvar4[i])
                        #verksvar4.remove(i)
                        break
                    else:
                        listinumer4.append(verksvar4[i])
                        listinumer4.append(verksvar4two[j])
        print(verksvar4)
        print(listinumer3)
        print(listinumer4)
        a = list(set(listinumer4))
        print(a)
        # call the function
        print(count)







        list1 = [6, 1, 5, 2, 3]
        list2 = [3, 5, 2, 1, 4]

        #def compare(list1, list2):

            # Check if all the elements of both the lists are same
        count = 0
        for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i] == list2[j]:
                        count += 1
                        
                        break
        

        # call the function
        print(count)
        #print(compare(list1, list2))
        #print(compare(newlist, newlist2))


    elif(val==5):  
     svar = "nei"
    else:
     print("willa") 
print("valmyndin var keyrð",teljary)

