from dataclasses import replace
from random import*
from tkinter import END
from math import*


###############################################################################

#naaaaa="já"
#while naaaaa == "já" or naaaaa == "Já":
   
    #print("Sláðu inn 1 til að gefa nafn:")
    
   # print("Sláðu inn 2 til að stöðva keyrslu forrits:")
  #  val = int(input(": "))

 #   if(val==1):
    # djvvjd=input("gefðu fornafn: ")
   #  urhuo=input("gefðu eftirnafn: ")
  #   adgas=djvvjd.capitalize()
 #    heth=urhuo.capitalize()
#     if urhuo[-6:] == "dóttir" :
         
    #     print(" komdu sæl ",adgas,heth)
   #  elif urhuo[-3:] == "son":
  #       print(" komdu sæll ",adgas,heth)
 #    else:
    #    print("error")
 
   # elif(val==2):  
  #   naaaaa="noooo"
 #   else:
 #    print("willa") 
###############################################################################
#djvvjd=input("gefðu fornafn: ")
#urhuo=input("gefðu eftirnafn: ")

#print=djvvjd.capitalize()
#print=urhuo.capitalize()

###############################################################################

#print(randint(1,100))

#print(randrange(20,30))



###############################################################################

#nafmn=int(input("tala:"))
#na=-nafmn
#da="ja"
#while da == "ja": 
   # if nafmn > 0 and nafmn < 10:

  #      print(nafmn*"*")
        
 #       na+=1
#        nafmn-=1
    #else:
   #     da = input("rena aftur ja or no: ")
        
  #      print("alt í lægi")
 #       nafmn=int(input("tala:"))

#print("end")

###############################################################################
#da="ja"

###############################################################################

da="ja"
teljary=0
svar = "já"
while svar == "já" or svar == "Já":
    teljary += 1
    print("Sláðu inn 1 dæmi1:")
    print("Sláðu inn 2 dæmi2:")
    print("Sláðu inn 3 dæmi3:")
    print("Sláðu inn 4 til að stöðva keyrslu forrits:")
    val = int(input(": "))

    if(val==1):
     nafmn=int(input("tala:"))
     while da == "ja": 
      if nafmn > 0 and nafmn < 10:

        print(nafmn*"*")
        
        
        nafmn-=1
      else:
        da = input("rena aftur ja or no: ")
        
        print("alt í lægi")
        nafmn=int(input("tala:"))
    elif(val==2):
        print("valdir 2")
    elif(val==3):  
                naaaaa="já"
                while naaaaa == "já" or naaaaa == "Já":
                
                 print("Sláðu inn 1 til að gefa nafn:")
                        
                 print("Sláðu inn 2 til að stöðva keyrslu forrits:")
                 val = int(input(": "))

                 if(val==1):
                        djvvjd=input("gefðu fornafn: ")
                        urhuo=input("gefðu eftirnafn: ")
                        adgas=djvvjd.capitalize()
                        heth=urhuo.capitalize()
                        if urhuo[-6:] == "dóttir" :
                            
                            print(" komdu sæl ",adgas,heth)
                        elif urhuo[-3:] == "son":
                            print(" komdu sæll ",adgas,heth)
                        else:
                            print("error")
                    
                 elif(val==2):  
                        naaaaa="noooo"
                 else:
                        print("willa") 
    elif(val==4):  
        svar = "nei"
    else:
        print("willa") 
print("valmyndin var keyrð",teljary)

###############################################################################
