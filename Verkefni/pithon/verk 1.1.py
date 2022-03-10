import datetime
from decimal import ROUND_FLOOR
from typing import DefaultDict

x = datetime.datetime.now()

print(x)
import datetime

x = datetime.datetime.now()
print(x.year,)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%C"))
print(x.month)
print(x.day)
print(x.year)












###########################################################################################

#nanf = input("gefðu nafn 1")

#nanu = input("gefðu nafn 2")

#if nanf == nanu:
#    print(nanf,"og",nanu," er sama nafnið")

#else: 
#    print (nanf,"og",nanu," er ekki sama nafnið")








###########################################################################################


#time = int(input("gefðu tölu sem er lægri en 0 eða hærri en 10"))

#if time >= 0 and time <= 10:
#    print("Þessi tala er ekki lægri en núll eða hærri en 10")

#else: 
#    print("Vel gert!")








###########################################################################################

#time = int(input())

#if time >= 0 and time <= 3:
#    print("Nú er daginn tekið að lengja.")
#elif time >= 4 and time <= 5:
#    print("Vorið er komið og grundirnar gróa.")
#elif time >= 6 and time <= 8:
#    print("Núna er sumarið komið með blóm í haga.")
#elif time >= 9 and time <= 10:
#    print("Núna er haustið gengið í garð.")
#elif time >= 11 and time <= 12:
#    print("Núna styttist í jólin")
#else: 
#    print("Rangur innsláttur")





###########################################################################################

#print("nu wellur þu :tom fyrir tommur :sent fyrir sentimetra:en gefðu first tölu")

#tomsent=int(input())


#co = input(" tom,sent: ")

#ult = 0
#if co == 'tom':
#    ult = tomsent * 2.54
#elif co == 'sent':
#    ult = tomsent * 0.394


#else:
#    print("skill ekki!")

#print(tomsent, co , ":", ult)

#print("{:.2f}".format( ult))

###########################################################################################
#mið1 = input()
#mið2 = input()
#mið3 = input()


#if(mið2>mið1 and mið1>mið3 or mið3>mið1 and mið1>mið2):
#    print(mið1, "er Miðju tala")
    
#if(mið1>mið2 and mið2>mið3 or mið3>mið2 and mið2>mið1):
#    print(mið2, "er Miðju tala")
    
#if(mið1>mið3 and mið3>mið2 or mið2>mið3 and mið3>mið1):
#    print(mið3, "er Miðju tala")



###########################################################################################
#r = int(input())
#f = r*r*3.1415
#print
#x = round(5.76543, 2)
#print("{:.2f}".format(f))

#####################################################################################
#print("gefðu mer aldur 3 vinna þinna")
#talavin1 = int(input())
#talavin2 = int(input())
#talavin3 = int(input())
#naa = ((talavin1+talavin2+talavin3)/3)
#print("{:.2f}".format(naa))
#####################################################################################




name = input("Enter name:")
print("name is: " + name)

print("welkcome",name)

print("kvað er uppahalds fag þit",name)
fag = input()
print("Velkomin i",fag," þetta verður skemmtileg önn hjá okkur",name)


print("gefðu mer 2 tolur",name)




tala1 = int(input())
tala2 = int(input())
print("suman er",tala1+tala2,"profum nu -")

ta= int(input())
te= int(input())

print(ta-te)

tala3 = int(input(" Firsta tala: "))
tala4 = int(input(" tale 2: "))

print("veldu nu kvaða aðgerð?")
ch = input(" +,-,*,/: ")

result = 0
if ch == '+':
    result = tala3 + tala4
elif ch == '-':
    result = tala3 - tala4
elif ch == '*':
    result = tala3 * tala4
elif ch == '/':
    result = tala3 / tala4
else:
    print("skill ekki!")


print(tala3, ch , tala4, ":", result)




















print("nu kemur heiltöludeiling")
tq= int(input())
fe=int(input())
print(tq//fe)

print("og nu sjaum viðafgang ef seinni tölu er deilt í fyrri tölu" )

deli=int(input())
teli=int(input())
print(deli%teli)




print("nu wellur þu")

ast=int(input())
ats=int(input())

cu = input(" //,%,&: ")

assult = 0
if cu == '//':
    assult = ast // ats
elif cu == '%':
    assult = ast % ats
elif cu == '&':
    assult = ast & ats

else:
    print("skill ekki!")



print(ast, cu , ats, ":", assult)

print("radius kulu")





radius = int(input(("slaðu in radius")))
yfirborð = radius*radius*3.14
print("flatarmal er ",yfirborð)
flaat=round(2 *radius*3.14)
print("Ummál hrings",flaat)




print("kwað er aldur faðirs þins ")
nafn1 = int(input())
print("kwað er aldur þins")
nafn2 = int(input())

print("pappi þin war ")


print(nafn1-nafn2)
print("þegar þu fædist")






print("gefðu mer aldur 3 vinna þinna fyrir meðal aldur")

talavin1 = int(input())
talavin2 = int(input())
talavin3 = int(input())

naa = ((talavin1+talavin2+talavin3)/3)
print("meðal aldur er")
print("{:.2f}".format(naa))




print("miðju tala af 3")
mið1 = int(input())
mið2 = int(input())
mið3 = int(input())


if(mið2>mið1 and mið1>mið3 or mið3>mið1 and mið1>mið2):
    print(mið1, "er Miðju tala")
    
if(mið1>mið2 and mið2>mið3 or mið3>mið2 and mið2>mið1):
    print(mið2, "er Miðju tala")
    
if(mið1>mið3 and mið3>mið2 or mið2>mið3 and mið3>mið1):
    print(mið3, "er Miðju tala")




print("nu wellur þu :tom fyrir tommur :sent fyrir sentimetra:en gefðu first tölu")

tomsent=int(input())


co = input(" tom,sent: ")

ult = 0
if co == 'tom':
    ult = tomsent * 2.54
elif co == 'sent':
    ult = tomsent * 0.394


else:
    print("skill ekki!")

print(tomsent, co , ":", ult)

print("{:.2f}".format( ult))




time = int(input("gefðu mánuð"))

if time >= 0 and time <= 3:
    print("Nú er daginn tekið að lengja.")
elif time >= 4 and time <= 5:
    print("Vorið er komið og grundirnar gróa.")
elif time >= 6 and time <= 8:
    print("Núna er sumarið komið með blóm í haga.")
elif time >= 9 and time <= 10:
    print("Núna er haustið gengið í garð.")
elif time >= 11 and time <= 12:
    print("Núna styttist í jólin")
else: 
    print("Rangur innsláttur")





time = int(input("gefðu tölu sem er lægri en 0 eða hærri en 10"))

if time >= 0 and time <= 10:
    print("Þessi tala er ekki lægri en núll eða hærri en 10")

else: 
    print("Vel gert!")






nanf = input("gefðu nafn 1")

nanu = input("gefðu nafn 2")

if nanf == nanu:
    print(nanf,"og",nanu," er sama nafnið")

else: 
    print (nanf,"og",nanu," er ekki sama nafnið")