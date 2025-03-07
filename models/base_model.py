#!/usr/bin/python3
import uuid
import time
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        print("{} {} {}".format(BaseModel.__name__ , self.id , self.__dict__))

    def save(self):
        updated_at = datetime.now()


    def to_dict(self):
        return self.__dict__

if __name__ == "__main__":
    a = BaseModel()
    a.__str__
