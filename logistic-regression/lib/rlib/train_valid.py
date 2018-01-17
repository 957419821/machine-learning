from numpy import random, array, concatenate

# class to contain 3 methods to divide data into test and valid set
class train_valid():
    def __init__(self):
        self.hold_out_rate = 0.8
        self.cross_validation_k = 10
    def hold_out(self, data):
        # 80% training set and 20% validation set
        M = len(data); seperate = int(self.hold_out_rate * M)
        return data[0:seperate, :], data[seperate:, :]
    def cross_validation(self, data, i):
        # 10-fold cross validation
        delta = len(data)//self.cross_validation_k
        # get the ends of the validation set
        start = i * delta; end = start + delta
        if i == 0:
            return data[end:, :], data[0:end]
        elif i == self.cross_validation_k-1:
            return data[0: start, :], data[start:, :]
        elif i > 0 and i < self.cross_validation_k-1:
            return concatenate((data[0:start,:], data[end:,:]), axis=0), data[start:end,:]
        else:
            print(":::::::::::::  error: i is out of range")
    def bootstrapping(self, data):
        M = len(data)        
        # to sample the set, I use Python's class set
        # getting sample
        total_set = set(i for i in range(M))
        sample_index = [int(random.rand()*M) for i in range(M)]
        sample_set = set(sample_index)
        validation_set = total_set - sample_set
        # getting train set
        train = []
        for i in sample_index:
            train.append(data[i])
        # getting validation set
        validation = []
        for i in validation_set:
            validation.append(data[i])
        # return them
        return array(train), array(validation)

