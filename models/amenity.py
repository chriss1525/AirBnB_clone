#!/usr/bin/env python3
"""
This is a user model that describes the user
This model inherits from base_model.py

Public class attributes:
  - email: string - empty string
  - password: string - empty string
  - first_name: string - empty string
  - last_name: string - empty string
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This model defines the user
    it inherits from BaseModel
    """

    name = ""
