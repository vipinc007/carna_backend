import pickle
from data_manager import data_manager
import random
import os

class object_manager():
    data_file_name = 'just_some_data'

    def __init__(self, data_file):
        self.data_file_name=data_file

    def object_create(self):
        dm = data_manager(self.data_file_name)
        values = dm.unpickle_data()
        values["counter"] = values["counter"] + 1
        values["obj"].append(int(values["counter"]))
        dm.pickle_data(values)
        return True


    def object_reset(self):
        dm = data_manager(self.data_file_name)
        objs = []
        dm.pickle_data({"obj": objs, "counter": len(objs)})
        return True

    def object_get(self):
        dm = data_manager(self.data_file_name)
        values = dm.unpickle_data()
        obj = None
        if len(values["obj"]) > 0:
            obj = random.choice(values["obj"])
            values["obj"].remove(obj)
            dm.pickle_data(values)
        return obj

    def object_list(self):
        dm = data_manager(self.data_file_name)
        values = dm.unpickle_data()
        return values["obj"]

    def object_free(self,num):
        dm = data_manager(self.data_file_name)
        values = dm.unpickle_data()
        values["obj"].append(int(num))
        values["obj"].sort()
        dm.pickle_data(values)
        return True

    def delete_data_file(self):
        if os.path.exists(self.data_file_name):
            os.remove(self.data_file_name)