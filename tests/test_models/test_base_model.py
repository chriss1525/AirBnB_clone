#!/usr/bin/python3
"""This test module defines tests for base_model.py"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_save_updates_updated_at(self):
        """Create an instance of BaseModel"""
        model = BaseModel()

        """Save the model"""
        model.save()

        """Get the updated_at attribute"""
        updated_at = model.updated_at

        """Check that updated_at has been updated"""
        self.assertNotEqual(model.created_at, updated_at)

    def test_to_dict_contains_all_attributes(self):
        """Create an instance of BaseModel"""
        model = BaseModel()

        """Convert the model to a dictionary"""
        model_dict = model.to_dict()

        """Check that the dictionary contains all expected keys"""
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_datetime_formatting(self):
        """Create an instance of BaseModel"""
        model = BaseModel()

        """Convert the model to a dictionary"""
        model_dict = model.to_dict()

        """Check that created_at and updated_at are in ISO format strings"""
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_id(self):
        """Create two BaseModel instances"""
        model1 = BaseModel()
        model2 = BaseModel()

        """Test that their ids are unique"""
        self.assertNotEqual(model1.id, model2.id)

        """Test that their ids are of the correct type"""
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)


if __name__ == '__main__':
    unittest.main()
