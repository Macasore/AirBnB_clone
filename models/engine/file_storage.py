#!/usr/bin/python3
"""file_storage file
this file contains the FileStorage class for
serialization and deserialization
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class
    this class contains the attribute and methods
    required for serializing and deserializing objects
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        instantiation method
        """

    def all(self):
        """
        returns a dictionary of available objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        adds the object to the existing file
        """
        FileStorage.__objects["{}.{}"
                              .format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes the object file
        """
        json_obj = {}
        for key, value in FileStorage.__objects.items():
            json_obj[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            json.dump(json_obj, fp, indent=2)

    def reload(self):
        """
        deserializes the json object
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_object = json.load(f)

                for key, value in json_object.items():
                    FileStorage.__objects[key] = BaseModel(**value)

        except Exception:
            pass
