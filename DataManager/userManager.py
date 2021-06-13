import pickle
from DataStore.storeKeeper import store_keeper
import random
import os

class user_manager():
    data_file_name = 'Users.data'

    def __init__(self, table_name="Users.data"):
        self.data_file_name = table_name
        self.store_keeper = store_keeper(self.data_file_name)

    def create(self,user_json):
        data_validation = self.__data_validation__(user_json)
        if data_validation is not None:
            return data_validation

        values = self.store_keeper.unpickle_data()
        if any(d.get('email', "").strip() == user_json["email"].strip() for d in values):
            return {"done": False, "message": "Email already exists"}

        nextid =1
        if len(values)>0:
            nextid = max([int(r["id"]) for r in values])
            nextid = nextid+1
        user_json["id"] = nextid
        values.append(user_json)
        self.store_keeper.pickle_data(values)

        return {"done":True,"message":"created","id":nextid}

    def edit(self,id,user_json):
        values = self.store_keeper.unpickle_data()
        if not any(int(d["id"])==int(id) for d in values):
            return {"done": False, "message": "Record does not exist"}

        data_validation = self.__data_validation__(user_json)
        if data_validation is not None:
            return data_validation

        if any(d.get('email', "").strip() == user_json["email"].strip() and int(d.get('id', ""))!=int(id) for d in values):
            return {"done": False, "message": "Email already exists"}

        rindex=0
        for idx, r in enumerate(values):
            if int(r['id'])==int(id):
                rindex=idx
                break
        values[rindex]["email"]=user_json["email"]
        values[rindex]["name"] = user_json["name"]
        values[rindex]["country"] = user_json["country"]
        self.store_keeper.pickle_data(values)

        return {"done":True,"message":"updated"}


    def reset(self):
        self.store_keeper.pickle_data([])
        return True

    def get(self,id):
        values = self.store_keeper.unpickle_data()
        if not any(int(d["id"]) == int(id) for d in values):
            return {"done": False, "message": "Record does not exist"}
        record = [r for r in values if int(r['id']) == int(id)][0]

        return {"done":True,"message":"fetched","data":record}

    def delete(self,id):
        values = self.store_keeper.unpickle_data()
        if not any(int(d["id"]) == int(id) for d in values):
            return {"done": False, "message": "Record does not exist"}
        rindex = -1
        for idx, r in enumerate(values):
            if int(r['id']) == int(id):
                rindex = idx
                break
        values.pop(rindex)
        self.store_keeper.pickle_data(values)
        return {"done":True,"message":"deleted"}

    def list(self):
        values = self.store_keeper.unpickle_data()
        return {"done":True,"message":"fetched","data":values}


    def delete_data_file(self):
        self.store_keeper.delete_data_file()


    def __data_validation__(self,data):
        if data is None or len(data.items()) == 0:
            return {"done":False,"message":"Dataset is empty"}
        if "email" not in data.keys():
            return {"done":False,"message":"Email is required"}
        if data['email'] is None or len(data['email'].strip()) == 0:
            return {"done":False,"message":"Email cannot be null or empty"}
        if "name" not in data.keys():
            return {"done":False,"message":"Name is required"}
        if data['name'] is None or len(data['name'].strip()) == 0:
            return {"done":False,"message":"Name cannot be null or empty"}
        if "country" not in data.keys():
            return {"done":False,"message":"Country is required"}
        if data['country'] is None or len(data['country'].strip()) == 0:
            return {"done":False,"message":"Country cannot be null or empty"}
        return None