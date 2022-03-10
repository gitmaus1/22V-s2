svar = 'já'
while svar == 'já' or svar == 'Já':
    radius = int(input("Sláðu inn radís: "))
    print("Flatarmálið er:",  radius*radius*3.14)
    print()
    svar = input("Viltu reyna aftur já eða nei?: ")
