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

"""
Examples:
p.x + p.y = 33
p[0] + p[1] = 33
"""
