#!/usr/bin/python3
"""city file
Contains the City class that inherits from BaseModel
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    City class
    """
    name = ""
    state_id = ""
