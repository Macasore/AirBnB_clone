#!/usr/bin/env python3
"""
Test file containing test cases of the base model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """TestBaseModel
    tests the baseModel class
    """
    def test_attributes(self):
        """
        tests the attributes of the BaseModel class
        """
        base_1 = BaseModel()
        base_2 = BaseModel()

        self.assertIsInstance(base_1, BaseModel)  # check instance of objects
        self.assertIsInstance(base_1.id, str)  # check type of id
        self.assertIsInstance(base_1.created_at, datetime)
        self.assertIsInstance(base_2.updated_at, datetime)
        self.assertNotEqual(base_1.id, base_2.id)
        self.assertEqual(len(base_1.id), 36)  # checks the length of the id

    def test_save(self):
        """
        tests the save method
        """
        base3 = BaseModel()

        last_date = base3.updated_at
        base3.save()

        self.assertNotEqual(base3.updated_at, last_date)

    def test_to_dict(self):
        """
        tests the to_dict function
        """
        base = BaseModel()
        test_res = base.to_dict()

        self.assertEqual(test_res['created_at'], base.created_at.isoformat())
        self.assertIsInstance(test_res, dict)
        self.assertEqual(test_res['updated_at'], base.updated_at.isoformat())
        self.assertIsInstance(test_res['id'], str)
        self.assertIn('__class__', test_res)
        self.assertEqual(test_res['__class__'], "BaseModel")
