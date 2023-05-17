#!/usr/bin/python3
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User


avail_classes = {
    'BaseModel': BaseModel,
    'User': User
}
storage = FileStorage()
storage.reload()
