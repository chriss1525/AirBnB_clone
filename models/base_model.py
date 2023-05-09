#!/usr/bin/env python3
"""
This is our base model
takes in public instances attributes id,created_at 
and updated at.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel describes public instance attributes id, 
    created_at and updated at
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

model = BaseModel()
print(model)
