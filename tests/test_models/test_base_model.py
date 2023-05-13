#!/usr/bin/python3
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

    def test_ignore_args(self):
        """
        Test that args supplied when creating a
        new instance are ignored
        """

        base = BaseModel()
        base_dict = base.to_dict()

        new_base = BaseModel("hello", **base_dict)

        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.id, new_base.id)
        self.assertEqual(base.created_at, new_base.created_at)

    def test_create_from_dict(self):
        """
        Test that a new instance is successfully created from
        a dictionary using kwargs
        """

        base = BaseModel()
        base_dict = base.to_dict()

        new_base = BaseModel(**base_dict)

        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.id, new_base.id)
        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(str(base), str(new_base))

    def test_copy_all_dict_keys(self):
        """
        Test that all dictionary keys are
        copied to the new object including extra keys
        """

        base = BaseModel()
        base.name = "yam"
        base.occupation = "developer"

        base_dict = base.to_dict()

        new_base = BaseModel(**base_dict)

        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.id, new_base.id)
        self.assertEqual(new_base.name, "yam")
        self.assertEqual(new_base.occupatiom, "developer")
        self.assertEqual(base.created_at, new_base.created_at)

    def test_class_not_copied(self):
        """
        Test that the __class__ attribute from
        the dictionary was not copied
        """

        base = BaseModel()
        base_dict = base.to_dict()
        base_dict["__class__"] = "MyShittyClass"

        new_base = BaseModel(**base_dict)
        self.assertNotEqual(new_base.__class__, base_dict["__class__"])

    def test_missing_keys(self):
        """
        Test that an error is thrown when accessing attributes that weren't
        set when creating from dictionary
        """

        base = BaseModel()
        base_dict = {"id": "sfhfgjgdffg"}

        new_base = BaseModel(**base_dict)

        with self.assertRaises(Exception):
            val = new_base.created_at
            val = new_base.updated_at


if __name__ == "__main__":
    unittest.main()
