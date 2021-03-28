from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    email: str
    phone: str

@dataclass
class Car:
    manufacturer: str
    model: str
    year: int
    color: str

"""
Example:
contact = Contact("test","test@test.com","00 00 00 00")
"""

from collections import namedtuple

Point = namedtuple('Point', ["x", "y"])
p = Point(11, 22)

Person = namedtuple('Person', ["name", "age", "hobby"])
p2 = Person("Serjio", "40", "Video Games")
"""
Examples:
p.x + p.y = 33
p[0] + p[1] = 33

print(f"hello {p2.name}")
"""
