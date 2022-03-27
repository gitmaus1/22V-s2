




tölur=[2,4,7,8]
print(tölur)
tölur.append(100)
print(tölur)
tölur.insert(0,1)
print(tölur)
tölur.pop()
print(tölur)
del tölur[0]
print(tölur)
tölur.remove(7)
print(tölur)
texter= input("text: ")
if texter.isupper():
    print("ekki alir litlir stafir")
else:
    print("alir litlir stafir")
textur= input("isdigit text: ")
print(textur.isdigit())
texter= input("isalpha text: ")
print(texter.isalpha())
textrtr= input("count a text: ")
print(textrtr.count("a"))
