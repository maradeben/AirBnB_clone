#!/usr/bin/python3

"""This defines the Amenity Model
It inherit from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity Model"""

    # Attributes
    name: str = ""
