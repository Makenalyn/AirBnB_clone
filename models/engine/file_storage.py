#!/usr/bin/python3

""" class Filestorage that serializes instances to JSON file """


class FileStorage:

    """ private class attributes """
    def __init__(self):
        self.__file_path = ""
        self.__objects = [self.__class__.__name__.id]

    """ return the dictionary __objects """
    def all(self):
        return self.__dict__.__objects

    """ sets in __objects the obj with key <obj classname>.id """
    def new(self, obj):
        for key, value in __objects.items():
            key['obj'] = ob.__class__.__name__.id

    """ serializes __objects to the JSON file(path: __file_path) """
    def save(self):
        with open(__file_path, 'r+') as f:
            f.write(__objects.__dict__)

    """ deserializes the JSON file to __objects( only if the path exist
        no exception should be raised"""
    def reload(self):
        x = json.loads(__objects.__dict__)
