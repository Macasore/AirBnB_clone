#!/usr/bin/python3
from .engine.file_storage import FileStorage
from .base_model import BaseModel
storage = FileStorage()
storage.reload()

avail_classes = {
	'BaseModel': BaseModel
}
