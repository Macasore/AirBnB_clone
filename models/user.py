#!/usr/bin/python3
"""User file
contains the User class that inherits from basemodel
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    the User class contaians attributes required for users
    and inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
