#!/usr/bin/python3

class Filestorage:
    __file_path = "path"
    __objects = 0

    def all(self):
        return __objects.__dict__

    def new(self, obj):
        pass

    def save(self):
        return json.dumps(self)

    def reload(self):
        return json.dumps(self)
