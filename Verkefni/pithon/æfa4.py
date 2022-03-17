from dataclasses import replace


texti="1 2 3 4 5"
print(texti.count(" "))#telur bill
ddddd=input("skrifa: ")
print(ddddd.isupper())#ef stór true ef litil false
print(ddddd.islower())#ef litil true ef stór false
print(ddddd.swapcase())#stórir werða litlir litlir stórir
print(ddddd.replace(" "," ass "))
a1=input("a1: ")
a2=input("a2: ")
a3=input("a3: ")
a4=input("a4: ")
a5=input("a5: ")
b1=len(a1)
b2=len(a2)
b3=len(a3)
b4=len(a4)
b5=len(a5)
if b1 >= b2 and b1 >= b3 and  b1 >= b4 and b1 >= b5 :
    print("a1 stór")
    print(b1)
    print(a1)
elif b2 >= b1 and b2 >= b3 and  b2 >= b4 and b2 >= b5 :
    print("a2 stór")
    print(b2)
    print(a2)
elif b3 >= b1 and b3 >= b2 and  b3 >= b4 and b3 >= b5 :
    print("a3 stór")
    print(b3)
    print(a3)
elif b4 >= b1 and b4 >= b2 and  b4 >= b3 and b4 >= b5 :
    print("a4 stór")
    print(b4)
    print(a4)
elif b5 >= b1 and b5 >= b2 and  b5 >= b3 and b5 >= b4 :
    print("a5 stór")
    print(b5)
    print(a5)