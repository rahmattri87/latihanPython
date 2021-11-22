
# 1. Manipulasi sebuah bilangan  nilai dictionary
# diketahui     --->    a = {1,2,4,6,8,9,10,5,3,7}
# ketentuan     --->    a. urutkan bilangan dari terkecil hingga terbesar
#                             ---> a = {1,2,3,4,5,6,7,8,9,10}
#                       b. cari bilagan terkecil    ---> 1
#                       c. cari bilagan terbesar    ---> 10

# 2. periksa bilangan jika terdapat didalam sebuah nilai dictionary
# diketahui     ---> d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Ketentuan     --->    a. jika di input(9), maka hasil False (*check if exist)
#                       b. kelompokan bilangan ganjil   ---> d = {1: 10, 3: 30, 5: 50}
#                       c. kelompokan bilangan genap    ---> d = {2: 20, 4: 40, 6: 60}

# 3. Buatlah sebuah nilai dictionary yang menghasilkan data dari sebuah rumusan berikut :
# diketahui     ---> jika nilai input diberikan adalah 5
# ketentuan     ---> tentukan rumusan/logic program
# hasil print   ---> a. ---> d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# hasil print   ---> b. ---> d = {1: 13, 2: 25, 3: 37, 4: 49, 5: 61}

#--------------------------------------------------------------------------------------------#

a = [1,2,4,6,8,9,10,5,3,7]

b = sorted(a, reverse=False)
print("Urutan bilangan dari terkecil hingga terbesar a = ",b)

c = sorted(a, reverse=True)
print("Urutan bilangan dari terbesar hingga terkecil a = ",c)

print("bilangan terkecil = ",min(a))
print("bilangan terbesar = ",max(a))

#--------------------------------------------------------------------------------------------#

# Dictionary Comprehension
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

ganjil = dict(
        filter(lambda e:e[0] % 2 == 1, d.items()) 
    )
    
genap = dict(
        filter(lambda e:e[0] % 2 == 0, d.items()) 
    )    

print("Kelompok bilangan ganjil d = ",ganjil)
print("Kelompok bilangan genap d = ",genap)

#--------------------------------------------------------------------------------------------#

squares = {}
angka=int(input("\nMasukan Angka : "))

for x in range(angka):
    squares[x] = x*10
    
print("Kelompok squares A = ",squares)

incr = 3
for x in range(angka):
    squares[x] = ((x+1)*10) + incr
    incr = (incr + 2)
    
print("Kelompok squares B = ",squares)    


#--------------------------------------------------------------------------------------------#
