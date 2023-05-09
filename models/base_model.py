#!/usr/bin/python3
""" BaseModel module """
import uuid
import datetime


class BaseModel:
    """ The BaseModel from which all other models inherit """

    def __init__(self):
        """ initialize a Model, unique for each Model """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ print a model object """

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ update the updated_at variable """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ return dictonary containing all keys/values """
        the_dict = self.__dict__
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()

        return (the_dict)
