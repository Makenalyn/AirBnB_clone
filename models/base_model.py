#!/usr/bin/python3

import uuid
from datetime import datetime

""" A baseModel class which is the base of all other classes"""


class BaseModel:

    """ pyblic instance attributes """
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"
