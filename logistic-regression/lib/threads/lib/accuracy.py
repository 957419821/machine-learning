# get accuracy of model
def accuracy(X_valid, Y_valid, w, b, sigmoid):
    DATA_VALID_SIZE = len(X_valid)
    predict = sigmoid(X_valid, w, b)
    acc = 0
    for i in range(DATA_VALID_SIZE):
        if predict[i] > 0.5 and Y_valid[i] == 1 or predict[i] < 0.5 and Y_valid[i] == 0:
            acc += 1
    acc /= len(predict)
    return acc
