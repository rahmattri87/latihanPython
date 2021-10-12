# ulang = 10
#
# for i in range(ulang):
#     print ("Perulangan ke-" + str(i))



# item = ['kopi','nasi','teh','jeruk','Pop Ice']
#
# for isi in item:
#     print (isi)

jawab = 'ya'
hitung = 0
while(True):
    hitung += 1  # ---> bilangan = n +1
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break

print ("Total perulagan: " + str(hitung))