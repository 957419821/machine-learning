from threads.lib.initial_data import initial_data_train_valid
from threads.lib.sigmoid import sigmoid
from threads.lib.accuracy import accuracy
from threads.lib.initial_weights_bias import initial_weights_and_bias
from threading import Lock
from threads.lib.time_used import *
# Timing begin
time_start = Start()

def thread_cross_validation(data, tv, LOOP_TIMES, alpha, update):
    k = tv.cross_validation_k; acc = 0
    lock = Lock()
    for i in range(k):
        w, b = initial_weights_and_bias()
        x_train, y_train, x_valid, y_valid = initial_data_train_valid(data, tv, 'cross_validation_'+str(i))
        # train this model with SGD
        for step  in range(LOOP_TIMES):
            w, b = update(x_train, y_train, w, b, alpha, sigmoid)
        # sum each accuracy of different train-valid set
        acc += accuracy(x_valid, y_valid, w, b, sigmoid)
    # avarage accuracy
    acc /= k
    lock.acquire()
    try:
        print("---------------------------------------------------")
        print("weights: ", w, " bias: ", b)
        print("the accuracy of logistic regression with cross_validation: ", acc)
        print("---------------------------------------------------")
        # Timing end
        time_end = End()
        # show time used
        time_used(time_start, time_end, 'cross_validation')
    finally:
        lock.release()
