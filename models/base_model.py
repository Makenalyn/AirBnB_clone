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

    def save(self):
        """updates public instance created_at with current date"""
    pass

    def to_dict(self):
        return self.__class__.__dict__
