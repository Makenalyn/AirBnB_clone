#!/usr/bin/python3

import uuid
import datetime
from datetime import datetime

""" A baseModel class which is the base of all other classes"""


class BaseModel:
    """ public instance attributes """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        mydict = self.__dict__.copy()
        if kwargs:
            for i, j in mydict.items():
                print(i, j)

    def __str__(self):

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the current time of updated_at with most recent save """

        self.updated_at = datetime.now()

    def to_dict(self):

        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()

        return dict_repr


if __name__ == "__main__":
    a = BaseModel()
    a.name = "My first model"
    a.num = 89
    print(a)
    a.save()
    print(a)
