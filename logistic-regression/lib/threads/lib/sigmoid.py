from numpy import matmul, exp

# sigmoid function, can be used to compute the predicted value
def sigmoid(x, w, b):
    t = matmul(x, w) + b
    return 1/(1+exp(-t))

