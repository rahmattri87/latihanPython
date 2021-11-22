## Inheritance ##

from _typeshed import Self


class Person:
  def __init__(self, fname, lname): # --> constract
    self.firstname = fname	# --> properties1
    self.lastname = lname	# --> properties2

  def printname(self):		# function / method
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year): # --> constract
    super().__init__(fname, lname)	# --> call class Parents as Person
    self.graduationyear = year		# --> properties1

  def welcome(self):
    print("Selamat datang", self.firstname, self.lastname, "ke kelas python", self.graduationyear)

# uji = Person("Rahmat", "Tri")
# uji.printname()

student1 = Student("Rahmat Tri","Yunandar",2021)
student1.welcome()