from random import randint


class Phone:
    def __init__(self):
        self.number = randint(10000000000, 99999999999)


class Samsung(Phone):
    brand = "Samsung"
    os = "Android"


class Apple(Phone):
    brand = "Apple"
    os = "IOS"


new1 = Samsung()
print(new1.brand, new1.os, new1.number)
