#!/usr/bin/env python3
"""base_model file

This file contains the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class

    This class defines al common attributes/methods for
    other classes.
    """
    def __init__(self):
        """
        Instantiate the objects with necessary
        attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        returns a string representation of the
        BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        updated_dict = self.__dict__.copy()
        updated_dict['__class__'] = self.__class__.__name__
        updated_dict['created_at'] = self.created_at.isoformat()
        updated_dict['updated_at'] = self.updated_at.isoformat()
        return (updated_dict)
