import os
import requests
from prettytable import PrettyTable
import json

print("============================WELCOME================================")
print("===================>>> TO OUR PRESENTATION <<<=====================")
print("\tPROJECT UTS SEMESTER 1 DASAR PEMROGRAMAN KELOMPOK 2\t\t")

pTable = PrettyTable()
pTable.field_names = ['No','Nama Mahasiswa/i','NIM','Kelas']
pTable.add_row(['01','ALFIA ZAHRA','19211183','19.1C.01'])
pTable.add_row(['02','DIMAS SAKTI','19210091','19.1C.01'])
pTable.add_row(['03','MUHAMMAD AFIF','19210534','19.1C.01'])
pTable.add_row(['04','RIDHO OKTRIAN PAMUNGKAS','19210840','19.1C.01'])
pTable.add_row(['05','SHELLA NOVIANA WIJAYA PUTRI','19210983','19.1C.01'])
pTable.add_row(['06','SHELLI NOVIANI WIJAYA PUTRI','19210987','19.1C.01'])
print(pTable)
print("\n")

#OOP
def Indonesia():
    class Tentang:
        def __init__(self, nama, jum, prov):
            self.nama = nama
            self.jumlah = jum
            self.provinsi = prov

        def about(self):
            print(self.nama,"adalah salah satu negara kepulauan terluas di dunia. Bahkan, Indonesia terletak pada kawasan yang strategis.")
        
        def about2(self):
            print("Menurut data terbaru dari Kementerian Kelautan dan Perikanan,",self.nama,"memiliki",self.jumlah,"pulau, yang terdiri dari pulau besar dan kecil.") 
        
        def about3(self):
            print("Jumlah provinsi di",self.nama,"sendiri saat ini terdapat",self.provinsi,"provinsi")

    info = Tentang("Indonesia","16.771","34")
    info.about()
    info.about2()
    info.about3()

#API use requests
def provinsi():
    url = "http://www.emsifa.com/api-wilayah-indonesia/api/provinces.json"
    Data =  requests.get(url).json()
    pTable = PrettyTable()
    pTable.field_names = ['No', 'ID Provinsi', 'Nama Provinsi']
    pTable.align['No'] = 'c'
    pTable.align['ID Provinsi'] = 'c'
    pTable.align['Nama Provinsi'] = 'c'

    no = 0
    for data in Data:
        no+=1
        pTable.add_row([no, data['id'], data['name'] ])
    print(pTable)
    print("\n")

#API in OOP    
def kabupaten():
    class Kabupaten:
        def __init__(self, url):
            self.url = url

        def mencari(self):
            Data = requests.get(self.url).json()
            self.data = Data

        def cetak(self):
            pTable = PrettyTable()
            pTable.field_names = ['ID', 'ID Kabupaten', 'Nama Kabupaten / Kota']
            pTable.align['ID'] = 'c'
            pTable.align['ID Kabupaten'] = 'c'
            pTable.align['Nama Kabupaten / Kota'] = 'c'

            for data in self.data['kota_kabupaten']:
                pTable.add_row([ data['id'], data['id_provinsi'], data['nama'] ])
            print(pTable)
            print("\n")

    call = Kabupaten("https://dev.farizdotid.com/api/daerahindonesia/kota?id_provinsi=32")
    call.mencari()
    call.cetak()

#API in OOP 
def kecamatan():
    class Kecamatan:
        def __init__(self, url):
            self.url = url

        def mencari(self):
            Data = requests.get(self.url).json()
            self.data = Data

        def cetak(self):
            pTable = PrettyTable()
            pTable.field_names = ['ID', 'ID Kecamatan', 'Nama Kecamatan']
            pTable.align['ID'] = 'c'
            pTable.align['ID Kecamatan'] = 'c'
            pTable.align['Nama Kecamatan'] = 'l'

            for data in self.data['kecamatan']:
                pTable.add_row([ data['id'], data['id_kota'], data['nama'] ])
            print (pTable)
            print("\n")

    call = Kecamatan("http://dev.farizdotid.com/api/daerahindonesia/kecamatan?id_kota=3214")
    call.mencari()
    call.cetak()

#API in OOP 
def kelurahan():
    class Kelurahan:
        def __init__(self, url):
            self.url = url

        def mencari(self):
            Data = requests.get(self.url).json()
            self.data = Data

        def cetak(self):
            pTable = PrettyTable()
            pTable.field_names = ['ID', 'ID Kelurahan', 'Nama Kelurahan']
            pTable.align['ID'] = 'c'
            pTable.align['ID Kelurahan'] = 'c'
            pTable.align['Nama Kelurahan'] = 'l'

            for data in self.data['kelurahan']:
                pTable.add_row([ data['id'], data['id_kecamatan'], data['nama'] ])
            print(pTable)
            print("\n")

    call = Kelurahan("https://dev.farizdotid.com/api/daerahindonesia/kelurahan?id_kecamatan=3214010")
    call.mencari()
    call.cetak()

def show_menu():
    print('======================================')
    print('===WILAYAH - WILAYAH INDONESIA' )
    print('======================================')
    print('1. Tentang Indonesia ')
    print('2. PROVINSI ')
    print('3. KABUPATEN / KOTA')
    print('4. KECAMATAN')
    print('5. KELURAHAN')
    print('0. Keluar')
    print('---------------------------------------')
    menu = input ("Pilih menu > ")

    os.system("cls")

    if menu == "1" :
        Indonesia()
    elif menu == "2":
        provinsi()
    elif menu == "3":
        kabupaten()
    elif menu == "4":
        kecamatan()
    elif menu == "5" :
        kelurahan()
    elif menu == "0":
       exit()
    else : 
        print ("Maaf tidak ada")

if __name__=="__main__" :
        while (True):
            show_menu()