#!/usr/bin/python3
import uuid
from datetime import datetime

"""
class model defining all common attributes/methods for other classes
"""


class BaseModel:

    datetime_now = datetime.now()

    def __self__(self, id):
        self.id = uuid.uuid4()
        self.created_at = datetime_now
        """self.updated is liable to update when object is changed"""
        self.updated_at = datetime_now

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        print ("{} {} {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.id = datetime.current()

    def to_dict(self):
        return dir(self)
