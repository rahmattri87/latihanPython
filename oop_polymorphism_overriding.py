from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "Bentuk bidang berupa dua dimensi."

    def __str__(self):
        return " --> " + self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Persegi memiliki sudut masing-masing sama dengan 90 derajat."

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

#initialize here
nilaiA = Square(4)
nilaiB = Circle(7)

print(f"Saya adalah {nilaiB}")
print(nilaiB.fact())
print(nilaiB.area())

print(f"Sekarang, saya menjadi sebuah {nilaiA}")
print(nilaiA.fact())
print(nilaiA.area())