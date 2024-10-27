import copy
from typing import NamedTuple

class Person(NamedTuple):
    name:str
    place:str
    version: str

person = Person(name="Geir Arne", place="Oslo", version="3.12")
print(person)

personreplaced = copy.replace(person, version="3.13")
print(personreplaced)
