import os
os.system('cls')

#Input
nama=input("Nama Karyawan:")
golongan_jabatan=input("Input Golongan Jabatan 1/2/3:")
pendidikan=input("Input Pendidikan SMA/D1/D3/S1:")
jam_kerja=int(input("Silahkan Input Jumlah Jam Kerja: "))
gaji_pokok=300000

#tunjangan jabatan
if golongan_jabatan=="1" :
    tunjangan_jabatan=(gaji_pokok)*0.05
elif golongan_jabatan=="2" :
    tunjangan_jabatan=(gaji_pokok)*0.1
else :
    tunjangan_jabatan=(gaji_pokok)*0.15

#tunjangan pendidikan
if pendidikan=="SMA" :
    tunjangan_pendidikan=(300000)*0.025
elif pendidikan=="D1" :
    tunjangan_pendidikan=(300000)*0.05
elif pendidikan=="D3" :
    tunjangan_pendidikan=(300000)*0.2
else :
    tunjangan_pendidikan=(300000)*0.3

#honor lembur
if jam_kerja >=8 :
    honor_lembur=(3500*jam_kerja)
else :
    honor_lembur=0

#TOTAL

total=(gaji_pokok)+(honor_lembur)+(tunjangan_pendidikan)+(tunjangan_jabatan)

#cetakhasil
print("===============================================")
print("         PROGRAM HITUNG GAJI KARYAWAN          ")
print("===============================================")
print("Karyawan Yang Bernama               :   "+str(nama))
print("Honor Yang Diterima                 :   "+str(gaji_pokok))
print("Tunjangan Jabatan                   :   "+str(tunjangan_jabatan))
print("Tunjangan Pendidikan                :   "+str(tunjangan_pendidikan))
print("Honor Lembur                        :   "+str(honor_lembur))
print("Total Gaji                          :   "+str(total))