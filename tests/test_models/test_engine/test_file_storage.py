#!/usr/bin/env python3
"""This test module defines tests for file_storage.py"""

import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test suite for the file_storage engine"""

    def test_save_objects_to_file(self):
        """Tests whether FileStorage can save JSON to a file"""

        # create new model
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        self.assertTrue(os.path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
