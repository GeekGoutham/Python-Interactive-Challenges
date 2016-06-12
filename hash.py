#Author = Vignesh Goutham
#Code to implement hash table in python
#Functions to set, get, erase items in hash table
#Hash table(not dictionary) takes in the input key, puts it through hash function which will output the location of
#the value to be stored
#Storage element would be an array or list in this case and indexing is used to achieve the O(1) complexity

#Here we are assuming the keys are integers alone for simplicity purposes.

class hash:
    def __init__(self):
        self.store_matrix = list()

    def set(self, key, value):
        self.store_matrix.insert(key, value)

    def get(self, key):
        return self.store_matrix[key]

    def erase(self, key):
        self.store_matrix.remove(key)