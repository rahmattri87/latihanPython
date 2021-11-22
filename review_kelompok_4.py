import requests
from prettytable import PrettyTable
import datetime
import os


class OpenApi:
    def __init__(self, url):
        self.url = url

    def GetData(self):
        requestData = requests.get(self.url).json()
        self.data = requestData

    def PrintData(self):
        pTable = PrettyTable()
        pTable.field_names = ['No', 'Product Name', 'Product Price']
        pTable.align['Product Name'] = 'l'
        pTable.align['Product Price'] = 'l'

        for data in self.data:
            pTable.add_row([data['id'], data['title'], data['price']])

        print(pTable)
        print("\r")

class Person:
    def __init__(self, name):
        self.name = name

    def title(self):
        print("Customer Name\t\t", self.name)
        date = datetime.datetime.now()
        print(date.strftime("%x\t\t%X"))

class Bill:
    def __init__(self, banyak, index, bayar):
        self.banyak = banyak
        self.index = index
        self.bayar = bayar

    def tabel(self):
        pTableOutput = PrettyTable()
        pTableOutput.field_names = ['No.', 'Product Name', 'Product Price', 'Lots of stuff', 'Total Price']
        self.ptable = pTableOutput

    def proses(self):
        for i in range(0, self.banyak):
            self.index = i + 1
            print("\rItem -" + str(self.index))
            product = input("Product Number\t: ")
            pcs = int(input("Pieces\t\t: "))
            print('\r')

            if product == '1':
                name_product = 'Fjallraven'
                price_pcs = 109.95
            elif product == '2':
                name_product = 'Mens Casual Premium Slim Fit T-Shirts'
                price_pcs = 22.3
            elif product == '3':
                name_product = 'Mens Cotton Jacket'
                price_pcs = 55.99
            elif product == '4':
                name_product = 'Mens Casual Slim Fit '
                price_pcs = 15.99
            elif product == '5':
                name_product = 'John Hardy Women s Legends'
                price_pcs = 695
            elif product == '6':
                name_product = 'Solid Gold Petite Micropave'
                price_pcs = 168
            elif product == '7':
                name_product = 'White Gold Plated Princess'
                price_pcs = 9.99
            elif product == '8':
                name_product = 'Pierced Owl Rose Gold Plated'
                price_pcs = 10.99
            elif product == '9':
                name_product = 'WD 2TB Elements Portable External'
                price_pcs = 64
            elif product == '10':
                name_product = 'SanDisk SSD PLUS 1TB Internal SSD'
                price_pcs = 109
            elif product == '11':
                name_product = 'Silicon Power 256GB SSD 3D NAND'
                price_pcs = 109
            elif product == '12':
                name_product = 'WD 4TB Gaming Drive Works'
                price_pcs = 114
            elif product == '13':
                name_product = 'Acer SB220Q bi 21.5 inches Full HD'
                price_pcs = 599
            elif product == '14':
                name_product = 'Samsung 49-Inch CHG90 144Hz'
                price_pcs = 999.99
            elif product == '15':
                name_product = 'BIYLACLESEN Women s 3-in-1 Snowboard Jacket'
                price_pcs = 56.99
            elif product == '16':
                name_product = 'Lock and Love Women s Removable Hooded'
                price_pcs = 29.95
            elif product == '17':
                name_product = 'Rain Jacket Women Windbreaker'
                price_pcs = 39.99
            elif product == '18':
                name_product = 'MBJ Women s Solid Short Sleeve Boat Neck V'
                price_pcs = 9.85
            elif product == '19':
                name_product = 'Opna Women s Short Sleeve Moisture'
                price_pcs = 7.95
            elif product == '20':
                name_product = 'DANVOUY Womens T Shirt'
                price_pcs = 12.99
            else:
                name_product = 'unknown items'
                price_pcs = 0

            total_price = pcs * price_pcs
            self.bayar = self.bayar + total_price

            rowOutput = [self.index, name_product, price_pcs, pcs, total_price]
            self.ptable.add_row(rowOutput)

    def struk(self):
        print('\r')
        print(self.ptable)
        print("Total Pay\t : $" + str(self.bayar))

Api = OpenApi("https://fakestoreapi.com/products")
Api.GetData()
Api.PrintData()

call = Bill((int(input("How Many Items : "))), 0, 0)
call.tabel()
call.proses()
callData = Person(input("Buyer\t: "))
os.system('cls')
callData.title()
call.struk()