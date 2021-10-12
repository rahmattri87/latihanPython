
def greeting(name):
    print(f"Hello, {name}")

greeting = lambda name: print(f"Hello, {name}")

greeting("Petani Kode")
greeting("Dian")
greeting("Ayu")

bilangan = [10,2,8,7,5,4,3,11,0,1]
filtered_result = map (lambda x: x*x, bilangan)
print(list(filtered_result))

genap = lambda x: x%2 == 0
print(list(filter(genap, bilangan)))

# map --> for indeks in range (len(bilangan))