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

##################################################################################
#exp í exp eru tilraunir til að leisa verkefnin oft án comenta














##################################################



#chek=0


#counttt=0

#counlist=[]

#teningalisti=[]


#xone=1
#xtwo=2
#xtree=3
#xfour=4
#xfim=5
#xsix=6


#for s in range(100):
 #   tenningar1=randint(1,6)
  #  tenningar2=randint(1,6)
   # if tenningar1==tenningar2:
    #    counttt+=1
     #   counlist.append(tenningar1)
        

#    sumateninga=tenningar1+tenningar1
 #   print("Kast teningur 1 = " ,tenningar1)
  #  print("Kast teningur 2 = " ,tenningar2)
   # print("Samtals: ",sumateninga)
    #chek+=1
#    print("Þessi samtala verður sett í listann sem kast",chek )

#    teningalisti.append(sumateninga)
#list_count = Counter(counlist)
#print(list_count)

#print( "sama tala kom upp á báða teningana: ",counttt," sinum")

#print('{}  kom upp á báða teningana {} sinum'.format(xone, list_count[xone]))

#print('{}  kom upp á báða teningana {} sinum'.format(xtwo, list_count[xtwo]))

#print('{}  kom upp á báða teningana {} sinum'.format(xtree, list_count[xtree]))

#print('{}  kom upp á báða teningana {} sinum'.format(xfour, list_count[xfour]))

#print('{}  kom upp á báða teningana {} sinum'.format(xfim, list_count[xfim]))

#print('{}  kom upp á báða teningana {} sinum'.format(xsix, list_count[xsix]))


#print(counttt)
#print(counlist)



#print(teningalisti)
#raðaður = sorted(teningalisti)                #list(set(teningalisti))
#print(raðaður)
#Heildarsumma=sum(teningalisti)
#print(Heildarsumma)











##################################################




#nafn=input("gefðu nafn: ")
#kin=input("gefðu kin kk eða kvk: ")
#þingd=int(input("Hvað ertu þungur í kílóum: " ))
#print(nafn,end="")
#hæð=int(input(" sláðu inn hæð þína í metrum: "))

#bmi=þingd/(hæð*hæð)

#print("BMI stuðull þinn er" ,"{:.0f}".format(bmi))

#print("Þú er of þungur miðað við hæð", nafn, "(greinilega ekkert að marka þennan stuðul:-)")









##################################################

#stjorn= "j"

#input("itu á eitkvað til að rúla")
#teningur1=randint(1,6)
#teningur2=randint(1,6)

#summateningur=0

#print(teningur1)
#utttcoma1 = teningur1+teningur2


#if utttcoma1== 7 or utttcoma1== 11:
#        print(" winur")
#        stjorn= "k"

#if utttcoma1== 2 or utttcoma1== 3 or utttcoma1== 12:
#        print(" tapar")
#        stjorn= "k"
#stjorn= "k"

#summateningur=0

#summateningur+=utttcoma1

#if utttcoma1== 4 or utttcoma1== 5 or utttcoma1== 6 or utttcoma1== 8 or utttcoma1== 9 or utttcoma1== 10:
        
        #summateningur+=utttcoma1
#        print(" þú ert að rena að fá ",summateningur)


#while stjorn== "j":

#    input("itu á eitkvað til að rúla")

#    teningur1=randint(1,6)
#    teningur2=randint(1,6)


    

    #print(teningur1)
#    utttcoma1 = teningur1+teningur2


#    print("útcoma",utttcoma1)

#    if utttcoma1== 7 :
#        print(" tapar")
#        stjorn= "k"

#    if utttcoma1== summateningur :
#        print(" winur")
#        stjorn= "k"





##################################################

#teljara1=int(input("Sláðu inn teljara fyrir brot 1 = "))
#nefnara1=int(input("Sláðu inn nefnara fyrir brot 1 = "))
#teljara2=int(input("Sláðu inn teljara fyrir brot 2 = "))
#nefnara2=int(input("Sláðu inn nefnara fyrir brot 2 = "))





#utcoma=teljara1/nefnara1 * teljara2/nefnara2 


#utcoma2=teljara1*teljara2

#utcoma3=nefnara1*nefnara2
#while utcoma2 %2==0 and utcoma3 %2==0 :
#    utcoma2=utcoma2/2
#    utcoma3=utcoma3/2
    

#print(utcoma)

#x % 2 == 0



#print(teljara1,"/",nefnara1,"*",teljara2,"/",nefnara2,"=","{:.0f}".format(utcoma),"=","{:.0f}".format(utcoma2),"/","{:.0f}".format(utcoma3))





#input()
##################################################






#hsaq=input()
#work2=list(hsaq)
#print(work2)
#work3=[]


#IntVar = int("".join(filter(str.isdigit, hsaq)))
#print(IntVar)

#test_list = [8,5, "h", (5), 5,5," " ]+work2
#print(test_list)
#work=list(test_list)
#print(work)
#res = 0
#for ele in test_list:
#    if(isinstance(ele, int)):
#        work3.append(ele)
#        res += ele

#ses=0
#for e in work3:
    
        
#        ses += e



#print("Summa talna er : " + str(ses))
#print("Summa talna er : " + str(res))
#print(work3)
# printing result 
#print("Summa talna er : " + str(res))
##################################################
#svar4=input("svar4: ")


#int4 = int("".join(filter(str.isdigit, svar4)))
#print(int4)


# þeta verkefni er martröð
#sum_digit = 0
#for x in svar4:
 #   if x.isdigit():
#        sum_digit += int(x)


#print("Summa talna er : ", sum_digit)






















#skiftir út
#res1=re.sub(r'[A-Z]', '_', svar4) 
#res2 = re.sub(r'[" "]', "?", res1)


#utcoma=res1+res2

#print(res2)



#input()

##################################################
#def draw_hangman(wrong,board):
     
#    if wrong == 0:
 #       print(board)
         
  #  elif wrong == 1:
#        print ("     ______")
 #       print ("    |/")
  #      print ("    |")
   #     print ("    |")
#        print ("    |")
 #       print ("   _|_")
  #      print(board)
 
#    elif wrong == 2:       
 #       print ("     ______")
  #      print ("    |/")
   #     print ("    |   o  ")
    #    print ("    |")
     #   print ("    |")
      #  print ("   _|_")
       # print(board)   
#    elif wrong == 3:       
 #       print ("     ______")
  #      print ("    |/")
   #     print ("    |   o  ")
    #    print ("    |   |")
     #   print ("    |")
      #  print ("   _|_")
       # print(board)   
#    elif wrong == 4:       
 #       print ("     ______")
  #      print ("    |/")
   #     print ("    |  _o  ")
    #    print ("    |   |")
     #   print ("    |")
      #  print ("   _|_")
       # print(board) 
#    elif wrong == 5:       
 #       print ("     ______")
  #      print ("    |/")
   #     print ("    |  _o ")
    #    print ("    |   |")
     #   print ("    |  /")
      #  print ("    |")
       # print ("    |")
        #print(board) 
#    elif wrong == 6:       
 #       print ("     ______")
  #      print ("    |/")
   #     print ("    |  _o_ ")
    #    print ("    |   |")
     #   print ("    |  /")
      #  print ("   _|_")
       # print(board)   
#    elif wrong == 7:       
 #       print ("     ______")
  #      print ("    |/")
   #     print ("    |  _o_ ")
    #    print ("    |   |")
     #   print ("    |  / \\")
      #  print ("   _|_")
         
#    elif wrong == 8:
 #       print ("     ______")
  #      print ("    |/  |")
   #     print ("    |  _o_ ")
    #    print ("    |   |")
     #   print ("    |  / \\")
      #  print ("   _|_")
       # print(board)
        #print("þú tapar")     
         
#def get_letter(guesses):
 
 #   ok = True
  #  while ok:    
   #     try:
    #        letter = input("gefðu staff: ")
     #       if letter in guesses:
      #          print("hefur þegar verið notað")
       #     elif not letter.isalpha():
        #        print("akki stafur")
         #   elif len(letter) == 1:
          #      letter = letter.lower()
           #     break
#        except:
 #           print("reindu aftur")
  #  return letter        
        
#def set_up():
 
#    answe = ["stack", "overflow", "rocks","pokemon", "hús","matur"]
#    answer= random.choice(answe)
    
                        
       
#    board = ""
 #   for ch in answer:
  #      if ch == " ":
   #         board = board + " "
    #    else:
     #       board = board + "-"
     
#    return answer,board   
 
#def check_guess(answer,board,letter,wrong):
 
 #   if letter not in answer:
  #      wrong = wrong + 1 
   # else:
    #    for i in range(len(answer)):
     #       if answer[i] == letter:
      #          board = board[:i] + letter + board[i+1:]
#    return board,wrong
             
#answer,board = set_up()
#guesses = ""
#wrong = 0
 
#for i in range(27):
 #   letter = get_letter(guesses)
  #  guesses = guesses + letter
   # board,wrong = check_guess(answer,board,letter,wrong)
    #draw_hangman(wrong,board)
#    if board == answer:
 #       print("þú vinur")
  #      break
   # elif wrong == 8:
    #    break

#################################

#control="ja"



#listrin=[]
#while control == "ja":
#    suma2=-1
#    suma=1
#    listrin.clear()
#    talapart2=int(input("Sláðu inn tölu: "))
    

#    btrrbrbtebt=abs(talapart2)


#    if talapart2==0:
#        control="stop"

#    for i in range(abs(talapart2)):
        
#     if talapart2>0:
#        listrin.append(suma)
#        suma+=1
#        talapart2-=1
#        def multiplyNumbers(lst):
#            product = 1
#            for x in lst:
#                product = product * x
#            return product
#        print(multiplyNumbers(listrin))
    
#     if talapart2<0:
#        listrin.append(suma2)
#        suma2-=1
#        talapart2+=1
#        def multiplyNumbers(lst):
#            product = 1
#            for x in lst:
#                product = product * x
#            return product
#        print(multiplyNumbers(listrin))





        
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


teljary=0
svar = "já"
while svar == "já" or svar == "Já":
    teljary += 1
    print("Sláðu inn 1 fyrir Bílar:: 2 fyrir Margföldunarruna:: 3 fyrir Snaran  ")
    print("Sláðu inn 4 fyrir Texti:: 5 fyrir Margföldun almennra brota:: 6 fyrir Teningaspilið Craps  ")
    print("Sláðu inn 7 fyrir Þyngdarstuðull:: 8 fyrir Teningar::")
    print("Sláðu inn 9 til að stöðva keyrslu forrits:")
    val = int(input(": "))
    print("valdir ",val)

    
 








##################################################################################
##Liður 1 – Bílar
    if(val==1):
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
    if(val==2):

        control="ja"



        listrin=[]
        while control == "ja":
            suma2=-1
            suma=1

            #clear tæmir lista
            listrin.clear()
            talapart2=int(input("Sláðu inn tölu: "))
            

            btrrbrbtebt=abs(talapart2)

            #stopar prógram
            if talapart2==0:
                control="stop"
            # ef + 
            for i in range(abs(talapart2)):
                
             if talapart2>0:
                listrin.append(suma)
                suma+=1
                talapart2-=1
                def multiplyNumbers(lst):
                    product = 1
                    for x in lst:
                        product = product * x
                    return product
                print(multiplyNumbers(listrin),end="*")
            #ef -
             if talapart2<0:
                listrin.append(suma2)
                suma2-=1
                talapart2+=1
                def multiplyNumbers(lst):
                    product = 1
                    for x in lst:
                        product = product * x
                    return product
                print(multiplyNumbers(listrin),end="*")





##################################################################################
##Liður 3 – Snaran
    if(val==3):

        def draw_hangman(wrong,board):


           #her er heingimaður
            if wrong == 0:
                print(board)



            elif wrong == 1:
                print ("    ")
                print ("    ")
                print ("    ")
                print ("    ")
                print ("    ")
                print ("   _ _")
                print(board)


            elif wrong == 2:
                print ("     ")
                print ("    ")
                print ("    ")
                print ("    ")
                print ("    ")
                print ("   _|_")
                print(board)

            elif wrong == 3:
                print ("     ")
                print ("    |")
                print ("    |")
                print ("    |")
                print ("    |")
                print ("   _|_")
                print(board)



            elif wrong == 4:
                print ("     ______")
                print ("    |")
                print ("    |")
                print ("    |")
                print ("    |")
                print ("   _|_")
                print(board)




            elif wrong == 5:
                print ("     ______")
                print ("    |/")
                print ("    |")
                print ("    |")
                print ("    |")
                print ("   _|_")
                print(board)
        
            elif wrong == 6:       
                print ("     ______")
                print ("    |/")
                print ("    |   o  ")
                print ("    |")
                print ("    |")
                print ("   _|_")
                print(board)   
            elif wrong == 7:       
                print ("     ______")
                print ("    |/")
                print ("    |   o  ")
                print ("    |   |")
                print ("    |")
                print ("   _|_")
                print(board)   
            elif wrong == 8:       
                print ("     ______")
                print ("    |/")
                print ("    |  _o  ")
                print ("    |   |")
                print ("    |")
                print ("   _|_")
                print(board) 
            elif wrong == 9:       
                print ("     ______")
                print ("    |/")
                print ("    |  _o ")
                print ("    |   |")
                print ("    |  /")
                print ("    |")
                print ("    |")
                print(board) 
            elif wrong == 10:       
                print ("     ______")
                print ("    |/")
                print ("    |  _o_ ")
                print ("    |   |")
                print ("    |  /")
                print ("   _|_")
                print(board)   
            elif wrong == 11:       
                print ("     ______")
                print ("    |/")
                print ("    |  _o_ ")
                print ("    |   |")
                print ("    |  / \\")
                print ("   _|_")
                print(board)
                
            elif wrong == 12:
                print ("     ______")
                print ("    |/  |")
                print ("    |  _o_ ")
                print ("    |   |")
                print ("    |  / \\")
                print ("   _|_")
                print(board)
                print("þú tapar orðið var ",answer)     
                


                
        def get_letter(guesses):
        
            ok = True
            while ok:    
                try:
                    letter = input("gefðu staff: ")
                    if letter in guesses:
                        print("hefur þegar verið notað")
                    elif not letter.isalpha():
                        print("akki stafur")
                    elif len(letter) == 1:
                        letter = letter.lower()
                        break
                except:
                    print("reindu aftur")
            return letter        
                
        def set_up():
        
            answe = ["stack", "overflow", "rocks","pokemon", "hús","matur"]
            answer= random.choice(answe)
            
                                
            
            board = ""
            for ch in answer:
                if ch == " ":
                    board = board + " "
                else:
                    board = board + "-"
            
            return answer,board   
        
        def check_guess(answer,board,letter,wrong):
        
            if letter not in answer:
                wrong = wrong + 1 
            else:
                for i in range(len(answer)):
                    if answer[i] == letter:
                        board = board[:i] + letter + board[i+1:]
            return board,wrong
                    
        answer,board = set_up()
        guesses = ""
        wrong = 0
        
        for i in range(27):
            letter = get_letter(guesses)
            guesses = guesses + letter
            board,wrong = check_guess(answer,board,letter,wrong)
            draw_hangman(wrong,board)
            if board == answer:
                print("þú vinur")
                break
            elif wrong == 12:
                break
        print("wrong ",wrong," sinnum")


##################################################################################
##Liður 4 – Texti
    if(val==4):

        svar4=input("svar4: ")


        int4 = int("".join(filter(str.isdigit, svar4)))
        print(int4)


        # þeta verkefni er martröð ég 
        sum_digit = 0
        for x in svar4:
            if x.isdigit():
                sum_digit += int(x)


        print("Summa talna er : ", sum_digit)





        #skiftir út
        res1=re.sub(r'[A-Z]', '_', svar4) 
        res2 = re.sub(r'[" "]', "?", res1)


        utcoma=res1+res2

        print(res2)



        input()


##################################################################################
##Liður 5 – Marföldun almennra brota
    if(val==5):

        teljara1=int(input("Sláðu inn teljara fyrir brot 1 = "))
        nefnara1=int(input("Sláðu inn nefnara fyrir brot 1 = "))
        teljara2=int(input("Sláðu inn teljara fyrir brot 2 = "))
        nefnara2=int(input("Sláðu inn nefnara fyrir brot 2 = "))





        utcoma=teljara1/nefnara1 * teljara2/nefnara2 


        utcoma2=teljara1*teljara2

        utcoma3=nefnara1*nefnara2
        while utcoma2 %2==0 and utcoma3 %2==0 :
            utcoma2=utcoma2/2
            utcoma3=utcoma3/2
            

        print(utcoma)

        #x % 2 == 0



        print(teljara1,"/",nefnara1,"*",teljara2,"/",nefnara2,"=","{:.0f}".format(utcoma),"=","{:.0f}".format(utcoma2),"/","{:.0f}".format(utcoma3))




##################################################################################
##Liður 6 – Teningaspilið Craps
    if(val==6):

        stjorn= "j"

        input("itu á eitkvað til að rúla")
        teningur1=randint(1,6)
        teningur2=randint(1,6)

        summateningur=0

        #print(teningur1)
        utttcoma1 = teningur1+teningur2


        if utttcoma1== 7 or utttcoma1== 11:
                print(" winur")
                stjorn= "k"

        if utttcoma1== 2 or utttcoma1== 3 or utttcoma1== 12:
                print(" tapar")
                stjorn= "k"
        #stjorn= "k"

        summateningur=0

        summateningur+=utttcoma1

        if utttcoma1== 4 or utttcoma1== 5 or utttcoma1== 6 or utttcoma1== 8 or utttcoma1== 9 or utttcoma1== 10:
                
                #summateningur+=utttcoma1
                print(" þú ert að rena að fá ",summateningur)


        while stjorn== "j":

            input("itu á eitkvað til að rúla")

            teningur1=randint(1,6)
            teningur2=randint(1,6)


            

            #print(teningur1)
            utttcoma1 = teningur1+teningur2


            print("útcoma",utttcoma1)

            if utttcoma1== 7 :
                print(" tapar")
                stjorn= "k"

            if utttcoma1== summateningur :
                print(" winur")
                stjorn= "k"





##################################################################################
##Liður 7 – Þyngdarstuðull:
    if(val==7):



        nafn=input("gefðu nafn: ")
        kin=input("gefðu kin kk eða kvk: ")
        þingd=int(input("Hvað ertu þungur í kílóum: " ))
        print(nafn,end="")
        hæð=int(input(" sláðu inn hæð þína í metrum: "))

        bmi=þingd/(hæð*hæð)

        print("BMI stuðull þinn er" ,"{:.0f}".format(bmi))

        bmistit="{:.0f}".format(bmi)

        if bmi<18.5:


            print("Þú er of ljetur miðað við hæð", nafn, "(greinilega ekkert að marka þennan stuðul:-)")
        elif bmi>=18.5 and bmi<=24.9:
            print("Þú ert í kjörðíngd miðað við hæð", nafn, "(greinilega ekkert að marka þennan stuðul:-)")
        elif bmi>=25.0 and bmi<=29.9:
            print("Þú er of þungur miðað við hæð", nafn, "(greinilega ekkert að marka þennan stuðul:-)")
        elif bmi>=30:
            print("Þú ert alt of þungur miðað við hæð", nafn, "(greinilega mikið að marka þennan stuðul:-)")


##################################################################################
##Liður 8 – Teningar

    if(val==8):

        chek=0


        counttt=0

        counlist=[]

        teningalisti=[]


        xone=1
        xtwo=2
        xtree=3
        xfour=4
        xfim=5
        xsix=6


        for s in range(100):
            tenningar1=randint(1,6)
            tenningar2=randint(1,6)
            if tenningar1==tenningar2:
                counttt+=1
                counlist.append(tenningar1)
                

            sumateninga=tenningar1+tenningar1
            print("Kast teningur 1 = " ,tenningar1)
            print("Kast teningur 2 = " ,tenningar2)
            print("Samtals: ",sumateninga)
            chek+=1
            print("Þessi samtala verður sett í listann sem kast",chek )

            teningalisti.append(sumateninga)
        list_count = Counter(counlist)


        #Hversu oft sama tala kom upp á báða teningana

        print( "sama tala kom upp á báða teningana: ",counttt," sinum")

        print('{}  kom upp á báða teningana {} sinum'.format(xone, list_count[xone]))

        print('{}  kom upp á báða teningana {} sinum'.format(xtwo, list_count[xtwo]))

        print('{}  kom upp á báða teningana {} sinum'.format(xtree, list_count[xtree]))

        print('{}  kom upp á báða teningana {} sinum'.format(xfour, list_count[xfour]))

        print('{}  kom upp á báða teningana {} sinum'.format(xfim, list_count[xfim]))
        #Hversu oft 6 kom upp á báða teningana
        print('{}  kom upp á báða teningana {} sinum'.format(xsix, list_count[xsix]))


        print(counttt)
        print(counlist)


        #Listinn óraðaður
        print(teningalisti)

        #Listinn raðaður
        raðaður = sorted(teningalisti)                
        print(raðaður)

        #Heildarsumma listans
        Heildarsumma=sum(teningalisti)
        print(Heildarsumma)







    elif(val==9):  
     svar = "nei"
    else:
     print("   ") 
print("valmyndin var keyrð",teljary)