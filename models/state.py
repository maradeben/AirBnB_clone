#!/usr/bin/python3

"""This  defines the State Model
It inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """The State Model"""

    # Attributes
    name: str = ""
