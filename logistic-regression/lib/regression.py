# Author: Liushuai tomeasure@foxmail.com 2018/01/17
from numpy import load, random
from rlib.update_coef import update_weights_bias_SGD as update
from rlib.train_valid import train_valid
from threading import Thread
from threads import thread_1, thread_2, thread_3

# get data from ../data/data.npy
# then shuffle it
data_dir = '../data/data.npy'
data = load(data_dir)
random.shuffle(data)
# set parameters of model
#     alpha contains learning rates: (lr_w, lr_b) 
alpha = (0.0001, 0.0001)
LOOP_TIMES = 20000
# get the object of class test_valid to divide original data
tv = train_valid()
t1 = Thread(target=thread_1.thread_hold_out, args=(data, tv, LOOP_TIMES, alpha, update))
t2 = Thread(target=thread_2.thread_cross_validation, args=(data, tv, LOOP_TIMES, alpha, update))
t3 = Thread(target=thread_3.thread_bootstrapping, args=(data, tv, LOOP_TIMES, alpha, update))
ts = [t1, t2, t3]
for t in ts:
    t.start()



