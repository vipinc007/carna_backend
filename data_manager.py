import pickle
import os

class data_manager():
    filename = 'just_some_data'

    def __init__(self, fname):
        self.filename=fname

    def pickle_data(self,data):
        outfile = open(self.filename, 'wb')
        pickle.dump(data,outfile)
        outfile.close()


    def unpickle_data(self):
        file = open(self.filename,'rb')
        new_data = pickle.load(file)
        file.close()
        return new_data