#!/usr/bin/python3
from base_model import BaseModel

class User(BaseModel):
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    """ update FileStorage to manage correctly serialization and
        deserialization of User """

    """ update console to allow show, create, destroy, update and all"""
