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


class Place(BaseModel):
    """
    This model defines the user
    it inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
