import os
from abc import abstractmethod

import requests
from prettytable import PrettyTable
import json


class Indonesia:
    def __init__(self, choose=''):
        # Attribute of Class Parent
        self.nama = "Indonesia"
        self.jumlah_pulau = "16.771"
        self.jumlah_provinsi = "34"
        self.type = choose

    def fact(self):
        print(
            self.nama, " adalah salah satu negara kepulauan terluas di dunia. Bahkan, ", self.nama,
            " terletak pada kawasan yang strategis." +
            "Menurut data terbaru dari Kementerian Kelautan dan Perikanan, ", self.nama, " memiliki", self.jumlah_pulau,
            " pulau, yang terdiri dari pulau besar dan kecil." +
            "Jumlah provinsi di ", self.nama, " sendiri saat ini terdapat ", self.jumlah_provinsi, " provinsi"
        )

    @abstractmethod
    def requestInfo(self, find=''):
        try:
            if (self.type == 'provinsi'):
                url = "http://www.emsifa.com/api-wilayah-indonesia/api/provinces.json"
                data = requests.get(url).json()
            elif (self.type == 'kabupaten'):
                url = "http://www.emsifa.com/api-wilayah-indonesia/api/regencies/" + find + ".json"
                data = requests.get(url).json()
            elif (self.type == 'kecamatan'):
                url = "http://www.emsifa.com/api-wilayah-indonesia/api/districts/" + find + ".json"
                data = requests.get(url).json()
            elif (self.type == 'kelurahan'):
                url = "https://emsifa.github.io/api-wilayah-indonesia/api/villages/" + find + ".json"
                data = requests.get(url).json()
        except:
            data = json.loads('[]')

        return data

    def __str__(self):
        return "Indonesia"

#This here, Inheritance Between Class Provinsi (child) and Indonesia (parents)
class Provinsi(Indonesia):
    def __init__(self):
        super().__init__("Provinsi")

    def requestInfo(self):
        area = Indonesia("provinsi")
        return area.requestInfo() #--> return data of JSON fro

    def view(self):
        pTable = PrettyTable()
        pTable.field_names = ['No', 'ID Provinsi', 'Nama Provinsi']
        no = 0
        for data in self.requestInfo():
            no += 1
            pTable.add_row([no, data['id'], data['name']])
        print(pTable)


class Kabupaten(Indonesia):
    def __init__(self, ID):
        super().__init__("Kabupaten")
        self.ID = ID

    def requestInfo(self):
        area = Indonesia("kabupaten")
        return area.requestInfo(self.ID)

    def view(self):
        pTable = PrettyTable()
        pTable.field_names = ['No', 'ID Kabupaten', 'Nama Kabupaten']
        no = 0
        for data in self.requestInfo():
            no += 1
            pTable.add_row([no, data['id'], data['name']])
        print(pTable)


class Kecamatan(Indonesia):
    def __init__(self, ID):
        super().__init__("Kecamatan")
        self.ID = ID

    def requestInfo(self):
        area = Indonesia("kecamatan")
        return area.requestInfo(self.ID)

    def view(self):
        pTable = PrettyTable()
        pTable.field_names = ['No', 'ID Kecamatan', 'Nama Kecamatan']
        no = 0
        for data in self.requestInfo():
            no += 1
            pTable.add_row([no, data['id'], data['name']])
        print(pTable)


class Kelurahan(Indonesia):
    def __init__(self, ID):
        super().__init__("Kelurahan")
        self.ID = ID

    def requestInfo(self):
        area = Indonesia("kelurahan")
        return area.requestInfo(self.ID)

    def view(self):
        pTable = PrettyTable()
        pTable.field_names = ['No', 'ID Kelurahan', 'Nama Kelurahan']
        no = 0
        for data in self.requestInfo():
            no += 1
            pTable.add_row([no, data['id'], data['name']])
        print(pTable)


class Menu:
    def __init__(self):
        pass

    def view(self):
        print("============================WELCOME================================")
        print("===================>>> TO OUR PRESENTATION <<<=====================")
        print('======================================')
        print('=== WILAYAH - WILAYAH INDONESIA ===')
        print('======================================')
        print('1. Tentang Indonesia ')
        print('2. PROVINSI ')
        print('3. KABUPATEN / KOTA')
        print('4. KECAMATAN')
        print('5. KELURAHAN')
        print('0. Keluar')
        print('---------------------------------------')
        menu = input("Pilih menu > ")
        # os.system("cls")
        os.system('cls' if os.name == 'nt' else 'clear')

        if menu == "1":
            negara = Indonesia()
            negara.fact()

        elif menu == "2":
            provinsi = Provinsi()
            provinsi.view()

        elif menu == "3":
            pilih = input("Masukan ID Kabupaten > ")
            kabupaten = Kabupaten(pilih)
            kabupaten.view()

        elif menu == "4":
            pilih = input("Masukan ID Kecamatan > ")
            kecamatan = Kecamatan(pilih)
            kecamatan.view()

        elif menu == "5":
            pilih = input("Masukan ID Kelurahan > ")
            kelurahan = Kelurahan(pilih)
            kelurahan.view()

        elif menu == "0":
            exit()

        else:
            print("Maaf tidak ada")

        self.finish()

    def run(self):
        program = Menu()
        program.view()

    def finish(self):
        print("\n")
        jawab = input("Ulang lagi tidak [Yes/No] > ")
        if jawab == 'Yes' or jawab == 'Y' or jawab == 'y':
            # os.system("cls")
            os.system('cls' if os.name == 'nt' else 'clear')
            self.run()
        else:
            exit()

#instance a Class Menu
program = Menu()
program.run()
