from random import *

# 2
minnEn45 = 0
minnstaTala = 101
summa = 0
for i in range(10):
    slembitala = randint(40,50)
    print(slembitala, end=" ")
    summa = summa + slembitala # Leggjum saman allar tölur    
    minnstaTala = min(minnstaTala,slembitala) # Finnum minnstu töluna

    if slembitala < 45:
        minnEn45 = minnEn45 + 1
        
print()
print(minnstaTala)
print(minnEn45)
