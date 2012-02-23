"""
Client that uses module `basic` (basic.py)
"""
from basic import *

print(adder(1, 7)) # should be 8
print(mult(3, 2)) # should be 6

me = Person('Fred', 'Galoso', 20)
girl = Girl('Sally', 'Mason', 61, 'sals', 'Husky')

print("What is in an object")
print(dir(object))
print("\n")

print("What is in a Person")
print(dir(me))
print("\n")

print("What is in a Girl, who happens to also be a Person, with a Dog mixed in")
print(dir(girl))
print("\n")

print(girl.set_breed('Husky'))
print(girl.is_of_breed('Husky'))
