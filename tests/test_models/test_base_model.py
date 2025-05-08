#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class Test_Base_Model(unittest.TestCase):

    """ test the uuid of the Class Model """

    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
