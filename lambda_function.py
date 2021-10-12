# Variabel global untuk menyimpan data Buku
buku = ["Komik","Science"]

# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print ("[%d] %s" % (indeks, buku[indeks]))

# fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

# fungsi untuk menhapus data
def delete_data():
    show_data()
    indeks = input("Inputkan ID buku: ")
    if(int(indeks) > len(buku)):
        print ("ID salah")
    else:
        buku.remove(buku[int(indeks)])

insert_data()
delete_data()
show_data()

if __name__ == "__main__":
    while (True):
       show_data()

