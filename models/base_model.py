#!/usr/bin/python3
import uuid
from models.engine import file_storage
from file_storage import FileStorage
import datetime
from datetime import datetime
""" A baseModel class which is the base of all other classes"""


class BaseModel:

    """instantiation of the public instance attributes """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    """ prints the class name, id and the dictionary of the instance """
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    """ updates the public instance updated_at with the current datetime """
    def save(self):
        self.updated_at = datetime.now()

    """ return the dictionary copy of the class instance """
    def to_dict(self):

        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()

        return dict_repr
