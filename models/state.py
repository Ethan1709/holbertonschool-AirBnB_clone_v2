#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models import storage


class State(BaseModel):
    """ State class """
    name = ""

def cities(self):
    cityl=[]
    for city in list(storage.all(City).values()):
        if city.state_id == self.id:
            cityl.append(city)
    return cityl