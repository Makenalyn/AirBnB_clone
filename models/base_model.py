#!/usr/bin/python3
import uuid
from datetime import datetime

"""
class model defining all common attributes/methods for other classes
"""


class BaseModel:

    datetime_now = datetime.now()

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        """self.updated is liable to update when object is changed"""
        self.updated_at = datetime.now()

    def __str__(self):
        return "{} {} {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return dir(self.__class__)
        created_at =  datetime.isoformat()
        updated_at = datetime.isoformat()
