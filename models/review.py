#!/usr/bin/python3

"""This file defines the review Model
 inherited from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Review Model"""

    # Attributes
    place_id: str = ""
    user_id: str = ""
    text: str = ""
