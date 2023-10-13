#!/usr/bin/python3
"""my json pack"""

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.____name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    obj = models[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

storage = FileStorage()
storage.reload()
