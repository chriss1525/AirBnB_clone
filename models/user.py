#!/usr/bin/env python3
"""This module contains the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a user model that describes the user
    This model inherits from base_model.py

    Public class attributes:
      - email: string - empty string
      - password: string - empty string
      - first_name: string - empty string
      - last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
