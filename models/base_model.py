#!/usr/bin/python3

import uuid
from datetime import datetime

""" A baseModel class which is the base of all other classes"""


class BaseModel:

    """ pyblic instance attributes """
    id = uuid.uuid4()
    created_at = datetime.now()
    updated_at = datetime.now()
