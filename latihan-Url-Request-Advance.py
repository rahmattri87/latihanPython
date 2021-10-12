import os
import requests
from prettytable import PrettyTable
import json

def print_to_table(data_table):

    print(f'Jumlah Data : {len(data_table)}')
    pTable = PrettyTable()
    pTable.field_names = ['Id.', 'Name', 'Email', 'Gender', 'Status', 'Created_at', 'Updated_at']
    pTable.align['Id'] = 'c'
    pTable.align['Name'] = 'l'
    pTable.align['Email'] = 'l'
    pTable.align['Gender'] = 'l'
    pTable.align['Status'] = 'l'
    pTable.align['Created_at'] = 'c'
    pTable.align['Updated_at'] = 'c'

    no = 0
    for i in data_table:
        no += 1
        row_details = [
            i['id'],
            i['name'],
            i['email'],
            i['gender'],
            i['status'],
            "i['created_at']",
            "i['updated_at']"
        ]
        pTable.add_row(row_details)

    print(pTable)
    print('\n\r')

def list_user():
    print('*** LIST ALL USER ***')

    url = "https://gorest.co.in/public-api/users"
    data = requests.get(url).text
    payload_data = json.loads(data)
    print_to_table(payload_data["data"])

def search_user():
    print('*** SEARCH USER BY ATTRIBUTE ***')
    print('----------------------------------------')

    attribute = input("Cari User Berdasarkan [name/email/id] > ")
    nilai = input("Masukan Nilai Pencarian > ")

    url = "https://gorest.co.in/public-api/users?" + attribute + "=" + nilai
    auth_token = '50ad7b086aad28845b356d7b4610f4775a29e61b413a2d6acc5e638c674a182a'
    hed = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + auth_token}

    response = requests.get(url, headers=hed)
    data = response.text
    payload_data = json.loads(data)
    print_to_table(payload_data["data"])


def create_user():
    print('*** CREATE NEW USER ***')
    print('----------------------------------------')

    url = 'https://gorest.co.in/public-api/users'
    auth_token = '50ad7b086aad28845b356d7b4610f4775a29e61b413a2d6acc5e638c674a182a'
    hed = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + auth_token}
    data = {
        "email": "rtrYESYES@ubsi.ac.id",
        "name": "rtr",
        "first_name": "rtr",
        "last_name": "Test",
        "gender": "Male",
        "status": "Active"
    }

    response = requests.post(url, json=data, headers=hed)
    data = response.text
    payload_data = json.loads(data)
    if payload_data["code"] == 201:
        print_to_table([payload_data["data"]])
    else:
        print(data)
        print('\n\r')


def update_user():
    print('*** UPDATE USER BY ID ***')
    print('----------------------------------------')

    user_id = input("Masukan ID User > ")
    status_kode = input("Masukan kode status [1/0] > ")

    url = 'https://gorest.co.in/public-api/users/' + user_id
    auth_token = '50ad7b086aad28845b356d7b4610f4775a29e61b413a2d6acc5e638c674a182a'
    hed = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + auth_token}

    if status_kode == '1':
        status = "Active"
    else:
        status = "Inactive"

    data = {
        "status": status
    }

    response = requests.put(url, json=data, headers=hed)
    data = response.text
    payload_data = json.loads(data)

    if payload_data["code"] == 200:
        print_to_table([payload_data["data"]])
    else:
        print(data)
        print('\n\r')


def delete_user():
    print('*** DELETE USER BY ID ***')
    print('----------------------------------------')

    user_id = input("Masukan ID User > ")

    url = 'https://gorest.co.in/public-api/users/' + user_id
    auth_token = '50ad7b086aad28845b356d7b4610f4775a29e61b413a2d6acc5e638c674a182a'
    hed = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + auth_token}

    response = requests.delete(url, headers=hed)
    data = response.text
    payload_data = json.loads(data)
    if payload_data["code"] == 204:
        print('Succes Delete User ID = ' + user_id)
        print('\n\r')
    else:
        print(data)
        print('\n\r')

def show_menu():
    print('========================================')
    print('=== SISTEM INFORMASI DATA USER ===')
    print('========================================')
    print('1. List All User')
    print('2. Search User By Attribute ')
    print('3. Create New User')
    print('4. Update User')
    print('5. Delete User')
    print('0. Keluar')
    print('----------------------------------------')
    menu = input("Pilih menu > " )

    os.system('cls')

    if menu == "1":
        list_user()
    elif menu == "2":
        search_user()
    elif menu == "3":
       create_user()
    elif menu == "4":
       update_user()
    elif menu == "5":
       delete_user()
    elif menu == "0":
       exit()
    else:
       print("Menu pilihan anda salah !!!!!")
       print("Silahkan ulangi kembali ...")

if __name__ == "__main__":
    while (True):
       show_menu()