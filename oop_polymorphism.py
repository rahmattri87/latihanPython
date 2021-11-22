## Polymorphism in Python ##

## example 1

# def add(x, y, z = 0):
#     return x + y+z
 
# # Driver code
# print(add(2, 3))
# print(add(2, 3, 4))

## example 2

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Saya seekor kucing. Saya dipanggil {self.name}. Umur saya {self.age} tahun.")

    def make_sound(self):
        print("Meow... meow..")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Saya seekor Anjing. Saya dipanggil {self.name}. Umur saya {self.age} tahun.")

    def make_sound(self):
        print("Bark... grrr...")

cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()