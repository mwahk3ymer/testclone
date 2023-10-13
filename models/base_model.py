#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

class BaseModel:
"""A base class for all hbnb models"""

	def save(self):
            """Call save(self) method of storage."""
            storage.save()

	def __init__(self, *args, **kwargs):
		if kwargs:
            		for key, value in kwargs.items():
                	if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
	    storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        data['__class__'] = self.__class__.__name__
        return data

    @classmethod
    def from_dict(cls, data):
        if "__class__" in data:
            class_name = data["__class__"]
            if class_name == "BaseModel":
                instance = cls()
                for key, value in data.items():
                    if key == 'created_at' or key == 'updated_at':
                        setattr(instance, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(instance, key, value)
                return instance
            # Handle other classes derived from BaseModel here
        return None
