#!/usr/bin/python3

import uuid
from datetime import datetime

""" A baseModel class which is the base of all other classes"""


class BaseModel:

    """ pyblic instance attributes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return("[{}] ({}) {}").format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_repr = self.__dict__.copy()

        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()

        return dict_repr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
