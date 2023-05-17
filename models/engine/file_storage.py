#!/usr/bin/python3
"""file_storage file
this file contains the FileStorage class for
serialization and deserialization
"""
import json
from models.base_model import BaseModel
from models.user import User


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
        obj = FileStorage.__objects.copy()
        for key, value in obj.items():
            obj[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            json.dump(obj, fp, indent=2)
            fp.close()

    def reload(self):
        """
        deserializes the json object
        """
        from models import avail_classes
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_object = json.load(f)
                f.close()

                for key, value in json_object.items():
                    FileStorage.__objects[key] = avail_classes[
                        value["__class__"]](**value)

        except Exception:
            pass
