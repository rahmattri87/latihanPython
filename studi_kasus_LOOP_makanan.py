import os
from prettytable import PrettyTable
os.system('cls')

#INPUT
print('========================================')
print('========= GEROBAK FRIED CHICKEN ========')
print('========================================')
pTable = PrettyTable()
pTable.field_names = ['Kode.', 'Jenis Potong', 'Harga']
pTable.align['Kode.'] = 'c'
pTable.align['Jenis Potong'] = 'r'
pTable.align['Harga'] = 'l'

row1 = ['D', 'Dada', 'Rp. 25.000.000.000.000.000.000.000.000.000.000.000.000']
row2 = ['P', 'Paha', 'Rp. 20.000']
row3 = ['S', 'Sayap', 'Rp. 15.000']

pTable.add_row(row1)
pTable.add_row(row2)
pTable.add_row(row3)

print(pTable)
print('\r')
print('----------------------------------------')

banyak=int(input("Banyak Jenis: "))
print('----------------------------------------')

pTableOutput = PrettyTable()
pTableOutput.field_names = ['No.', 'Jenis Potong', 'Harga Satuan', 'Banyak Beli', 'Jumlah Harga']
pTableOutput.align['No.'] = 'c'
pTableOutput.align['Jenis Potong'] = 'l'
pTableOutput.align['Harga Satuan'] = 'l'
pTableOutput.align['Banyak Beli'] = 'l'
pTableOutput.align['Jumlah Harga'] = 'l'

index = 0
jumlah_bayar = 0
pajak = 0
total_bayar = 0

for i in range(0, banyak):
    index = i + 1
    print("Jenis Ke -\t: "+str(index))
    kode_potongan=input("Kode Potongan\t: ")
    banyak_potongan=int(input("Banyak Potongan\t: "))
    print('\r')

    if kode_potongan == 'D' or kode_potongan == 'd' :
        nama_potongan = 'Dada'
        harga_satuan = 25000
    elif kode_potongan == 'P' or kode_potongan == 'p' :
        nama_potongan = 'Paha'
        harga_satuan = 20000
    elif kode_potongan == 'S' or kode_potongan == 's' :
        nama_potongan = 'Sayap'  
        harga_satuan = 15000
    else :
        nama_potongan = 'unknown'      
        harga_satuan = 0
    
    jumlah_harga = banyak_potongan * harga_satuan
    jumlah_bayar = jumlah_bayar + jumlah_harga

    rowOutput = [index, nama_potongan, harga_satuan, banyak_potongan, jumlah_harga]
    pTableOutput.add_row(rowOutput)

print('\r')
print(pTableOutput)
print("Jumlah Bayar\t : Rp."+str(jumlah_bayar))
pajak = 0.1 * jumlah_bayar
print("Pajak\t\t : Rp."+str(pajak))
total_bayar = jumlah_bayar + pajak
print("Total Pembayaran : Rp."+str(total_bayar))
print('\r')



