

#nanan=input("nafn:")
#arg=float(input("hæð 1 metrum:"))
#print(arg)
#if arg == 2:
#    print("þú ert 2 metra há 200cm")
#elif arg >= 2:
#    print("þú ert",arg-2,"metrum hæri og",(arg*100)-200,"cm ifir")
#elif arg <= 2:
#    print("þú ert",arg-2,"metrum lægri og",(arg*100)-200,"cm undir")





##################################################################################################################
nafn1 = input("gefðu nafn 1:")
aldur1= int(input("og aldur:"))
nanf2 = input("gefðu nafn 2:")
aldur2= int(input("og aldur:"))


if aldur1 == aldur2:
    print(nafn1,"og",nanf2," eru jafn gamlir")

elif aldur1 >= aldur2:
    print(nafn1,"er eldri en",nanf2)

elif aldur1 <= aldur2:
    print(nanf2,"er eldri en",nafn1)

#else: 
#    print (nanf,"og",nanu," er ekki sama nafnið")
#################################################################################################################
aldur= int(input("fæðingaræár:"))

if aldur % 2 == 0:
    print("slet tala og þú ert",2022-aldur)
else:
    print("ódatala og þú ert",2022-aldur)
#################################################################################################################
#100cm í 1metra
nanan=input("nafn:")
arg=float(input("hæð 1 metrum:"))
print(arg)
if arg == 2:
    print(nanan," er 2 metra há 200cm")
elif arg >= 2:
    print(nanan," er",arg-2,"metrum hæri og",(arg*100)-200,"cm ifir")
elif arg <= 2:
    print(nanan,"er",arg-2,"metrum lægri og",(arg*100)-200,"cm undir")

################################################################################################################

print("gefðu 4 tölur")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
ax=(a+b+c)-d
print(ax)
print("(",a,"+",b,"+",c,")","-",d,"=",ax)