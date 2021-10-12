# Chcek version --> pip -V
# download lib Request --> pip install requests
# download lib PrettyTable --> pip install PrettyTable || pip3 install PrettyTable

# import requests
#
# req = requests.get('https://tutsplus.com/')
# req.encoding  # returns 'utf-8'
# req.status_code  # returns 200
# req.elapsed  # returns datetime.timedelta(0, 1, 666890)
# req.url  # returns 'https://tutsplus.com/'
# req.history
#
# print(req.url)

import os
import requests
from prettytable import PrettyTable
import json

def total_indonesia():
    url = "https://api.kawalcorona.com/indonesia/"
    data = requests.get(url).text
    obj = json.loads(data)
    #print(data)
    #exit()
    for summary in obj:
        print('*** TOTAL COVID-19 INDONESIA')
        print('----------------------------------------')
        print(f'Positif   : {summary["positif"]}')
        print(f'Sembuh    : {summary["sembuh"]}')
        print(f'Meninggal : {summary["meninggal"]}')
        print(f'Dirawat   : {summary["dirawat"]}')
        print('----------------------------------------')

def detail_indonesia():
    print('*** DETAIL COVID-19 INDONESIA')
    url = "https://api.kawalcorona.com/indonesia/provinsi/"
    data = requests.get(url).text
    obj = json.loads(data)

    pTable = PrettyTable()
    pTable.field_names = ['No.', 'Propinsi', 'Positif', 'Sembuh', 'Meninggal', 'Dirawat']
    # Mengatur posisi text r=right, l=left, c=center
    pTable.align['No'] = 'r'
    pTable.align['Propinsi'] = 'l'
    pTable.align['Positif'] = 'r'
    pTable.align['Sembuh'] = 'r'
    pTable.align['Meninggal'] = 'r'
    pTable.align['Dirawat'] = 'r'

    no = 0
    for i in obj:
        no += 1 # --> no = no + 1
        row_details = [     no,
                            i['attributes']['Provinsi'],
                            i['attributes']['Kasus_Posi'],
                            i['attributes']['Kasus_Semb'],
                            i['attributes']['Kasus_Meni'],
                            ""
        ]
        pTable.add_row(row_details)

    print(pTable)

def total_dunia():
    print('*** TOTAL COVID-19 DUNIA')
    print('----------------------------------------')
    url = "https://api.kawalcorona.com/positif/"
    data = requests.get(url).text
    confirmed = json.loads(data)
    print(f'Confirmed : {confirmed["value"]}')
    url = "https://api.kawalcorona.com/sembuh/"
    data = requests.get(url).text
    recovered = json.loads(data)
    print(f'Recovered : {recovered["value"]}')
    url = "https://api.kawalcorona.com/meninggal/"
    data = requests.get(url).text
    deaths = json.loads(data)
    print(f'Deaths    : {deaths["value"]}')
    print('----------------------------------------')

def detail_dunia():
    print('*** DETAIL COVID-19 DUNIA')
    url = "https://api.kawalcorona.com/"
    data = requests.get(url).text
    obj = json.loads(data)

    pTable = PrettyTable()
    pTable.field_names = ['No.', 'Country/Region', 'Confirmed', 'Recovered', 'Deaths', 'Active']
    # Mengatur posisi text r=right, l=left, c=center
    pTable.align['No'] = 'r'
    pTable.align['Country/Region'] = 'l'
    pTable.align['Confirmed'] = 'r'
    pTable.align['Recovered'] = 'r'
    pTable.align['Deaths'] = 'r'
    pTable.align['Active'] = 'r'

    no = 0
    for i in obj:
        no += 1
        row_details = [no, i['attributes']['Country_Region'], i['attributes']['Confirmed'], i['attributes']['Recovered'], i['attributes']['Deaths'], i['attributes']['Active']]
        pTable.add_row(row_details)

    print(pTable)

def show_menu():
    print('========================================')
    print('=== SISTEM INFORMASI COVID-19 PYTHON ===')
    print('========================================')
    print('1. Total Indonesia')
    print('2. Detail Indonesia')
    print('3. Total Dunia')
    print('4. Detail Dunia')
    print('0. Keluar')
    print('----------------------------------------')
    menu = input("Pilih menu > " )

    # clear screen
    # os.system("clear")

    # os.system('cls' if os.name == 'nt' else 'clear')
    # os.system('cls||clear')
    os.system('cls')

    if menu == "1":
       total_indonesia()
    elif menu == "2":
       detail_indonesia()
    elif menu == "3":
       total_dunia()
    elif menu == "4":
       detail_dunia()
    elif menu == "0":
       exit()
    else:
       print("Menu pilihan anda salah !!!!!")
       print("Silahkan ulangi kembali ...")

if __name__ == "__main__":
    while (True):
       show_menu()