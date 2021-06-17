import json
import os
import sys
from db import Device


JSON_NAME = "devices.json"
FULL_PATH = os.getcwd()
JSON_PATH = os.path.join(FULL_PATH, JSON_NAME)


class JsonObj:
    def __init__(self, json_path):
        self.path = json_path
        # self.db_path = db_path
        self.data = self.load()


    def load(self):
        with open(self.path) as json_file:
            return json.load(json_file)


    def print(self):
        for key, val in self.data.items():
            print(f"{key}: {val}")
    

    def get(self):
        return self.data
    

    def get_specified(self, key):
        return self.data[key]


    def update(self):
        with open(self.path, "w") as json_file:
            json.dump(self.data, json_file, indent=4)


    def modify(self, key, option, val):
        if key in self.data:
            if option in self.data[key]:
                self.data[key][option] = val
                # d = Device(self.db_path)
                # d.insert((key, val))
                # d.close_conn()
                return True

            else:
                print("Error! Specified option does not exist!")
                return False
        else:
            print("Error! Speciefied key does not exist!")
            return False


    def add(self, key, option, val):
        if key not in self.data:
            if option not in self.data[key]:
                self.data[key][option] = val
                # d = Device()
                # d.insert((key, val))
                # d.close_conn()

            else:
                print("Error! Specified option already exists")
                return False
        else:
            print("Error! Specified key already exists!")
            return False


    def delete(self, key):
        if key in self.data:
            self.data.pop(key, None)
        else:
            print("Error! Specified key does not exists!")