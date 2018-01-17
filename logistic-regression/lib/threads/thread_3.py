from threads.lib.initial_data import initial_data_train_valid
from threads.lib.sigmoid import sigmoid
from threads.lib.accuracy import accuracy
from threads.lib.initial_weights_bias import initial_weights_and_bias
from threading import Lock
from threads.lib.time_used import *
# Timing begin
time_start = Start()
def thread_bootstrapping(data, tv, LOOP_TIMES, alpha, update):
    w, b = initial_weights_and_bias()
    x_train, y_train, x_valid, y_valid = initial_data_train_valid(data, tv, 'bootstrapping')
    lock = Lock()
    # train this model with SGD
    for step  in range(LOOP_TIMES):
        w, b = update(x_train, y_train, w, b, alpha, sigmoid)
    # evaluate this model with accuracy
    acc = accuracy(x_valid, y_valid, w, b, sigmoid)
    lock.acquire()
    try:
        print("---------------------------------------------------")
        print("weights: ", w, " bias: ", b)
        print("the accuracy of logistic regression with bootstrapping: ", acc)
        print("---------------------------------------------------")
        # Timing end
        time_end = End()
        # show time used
        time_used(time_start, time_end, 'bootstrapping')
    finally:
        lock.release()
