#!/usr/bin/python3
import uuid
from datetime import datetime

"""
class model defining all common attributes/methods for other classes
"""


class BaseModel:

    """ the init class method """
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['updated_at'] = self.updated_at.isoformat()
        object_dict['created_at'] = self.created_at.isoformat()
        return object_dict
