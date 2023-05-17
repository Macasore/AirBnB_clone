#!/usr/bin/python3
"""review file
Contains the Review class that inherits from BaseModel
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    """
    place_id = ""
    user_id = ""
    text = ""
