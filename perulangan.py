jawab = 'ya' #---> String
hitung = 0 #---> Integer
hitung2 = 3.14 #---> Float, Decimal, Real

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break

print ("Total perulagan: " + str(hitung))