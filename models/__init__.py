#!/usr/bin/python3
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State


avail_classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'Review': Review,
    'State': State,
}
storage = FileStorage()
storage.reload()
