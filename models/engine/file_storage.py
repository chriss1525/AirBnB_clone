#!/usr/bin/env python3
"""This module contains the class FileStorage"""
import json
import os


class FileStorage:
    """This class is responsible for the serialization of instances to JSON
     and deserialization of JSON to instances

    Private Class Attributes:
        __file_path: string - path to JSON file
        __objects: dictionary - empty but will store all objects by
                   <classname>.id

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <objclass name>.id
        save(self): serializes __objects to the JSON file
        reload(self): deserializes the JSON file to __objects
    """

    def __init__(self):
        """Initializes an instance and sets the values for the
        private properties"""

        self.__objects = {}
        self.__file_path = "file.json"

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with the key <objclassname>.id"""

        name = obj.__class__.__name__ + "." + obj.id
        self.__objects[name] = obj.to_dict()
        self.save()

    def destroy(self, obj):
        """destroys entry in __objects with the key <objclassname>.id"""

        name = obj.__class__.__name__ + "." + obj.id
        del self.__objects[name]
        self.save()

    def save(self):
        """serializes __objects to the JSON file __file_path"""

        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
