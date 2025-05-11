#!/usr/bin/python3
import json
import os
""" class Filestorage that serializes instances to JSON file """


class FileStorage:

    """ private class attributes """
    def __init__(self):
        if os.path.exists("AirBnB/file.json"):
            self.__file_path = "AirBnB/file.json"
        self.__objects = {}

    """ return the dictionary __objects """
    def all(self):
        return self.__objects

    """ sets in __objects the obj with key <obj classname>.id """
    def new(self, obj):
        for key, value in self.__objects.items():
            key['obj'] = self.__class__.__name__.id

    """ serializes __objects to the JSON file(path: __file_path) """
    def save(self):
        objects = json.dumps(self.__objects)

        with open(self.__file_path, "w") as f:
            f.write(objects)

    """ deserializes the JSON file to __objects( only if the path exist
        no exception should be raised"""
    def reload(self):
        if self.__file_path:
            file_x = json.loads(objects)

        return file_x
