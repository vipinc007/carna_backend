import pickle
import os

class store_keeper():
    filename = 'just_some_data'
    folder = 'Data'

    def __init__(self, fname):
        self.filename=fname
        # if not os.path.exists(self.folder):
        #     os.makedirs(self.folder)
        my_path = os.path.abspath(os.path.dirname(__file__))
        self.fpath = os.path.join(my_path, self.folder+"/"+self.filename)
        # print(self.fpath)

    def pickle_data(self,data):
        outfile = open(self.fpath, 'wb')
        pickle.dump(data,outfile)
        outfile.close()


    def unpickle_data(self):
        file = open(self.fpath,'rb')
        new_data = pickle.load(file)
        file.close()
        return new_data

    def delete_data_file(self):
        if os.path.exists(self.fpath):
            os.remove(self.fpath)