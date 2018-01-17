from numpy import random
# initial weights and bias stochasticly
def initial_weights_and_bias():
    w = random.rand(10) * 20
    b = random.rand() * 20
    return w, b
