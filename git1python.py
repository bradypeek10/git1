import time

class Person:
    def __init__(self, aa, bb, cc):
        self.name = aa
        self.age = bb
        self.id = cc
        self.street = ""
        self.city = ""
        self.zip = ""
        self.phone = ""

    def myname(self):
        print("Hello my name is " + self.name)

    def myage(self):
        print("Hello my age is " + str(self.age))

    def mynameplusage(self):
        print(self.name + ":" + str(self.age))


class car:
    def __init__(self, aa, bb, cc):
        self.make = aa
        self.model = bb
        self.maxspeed = cc

    def mymake(self):
        print(f"Make is {self.make}")

class Engine:
    def __init__(self, cyl, turbo, size, ty, hp):
        self.cylinder = cyl
        self.turbo = turbo
        self.size = size
        self.type = ty
        self.horsepower = hp

    def speed(self):
        if self.cylinder < 6 and self.horsepower < 250 and not self.turbo:
            print("Way too slow")
        else:
            print("Pretty fast man!")

    def engine_type(self):
        if self.type == "boxer":
            print('You are probably a subaru...')
        elif self.type == "V":
            print("You have the coolest engine.")
        else:
            print("Eh it's okay!")


class lovelypet:
    def __init__(self,a1,a2):
        self.species = a1
        self.color = a2

    def lovelypet(self):
        print("Pet color is:", self.color)
        print("Pet species is:", self.species)


