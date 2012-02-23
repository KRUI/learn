"""
Module documentation
@author Fredrick Galoso
"""
'''
Block quote
    Basic module, function, and class tutorial
'''
def adder(x, y):
    return x + y

def mult(x, y):
    return x * y

class Person(object):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

class Dog(object):
    def __init__(self, nickname, breed):
        self.breed = ''

    def is_of_breed(self, breed):
        return breed == self.breed

    def set_breed(self, breed):
        self.breed = breed
        return self.breed

class Girl(Person, Dog):
    def __init__(self, firstname, lastname, age, nickname, breed):
        self.dog = Dog(nickname, breed)

    def is_girl(self):
        return True
