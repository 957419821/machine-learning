# Program:
#    generate data with Gaussian Distribution
#    and restore these data into ../data/data.npy
#    used for binary classification
# Author: Liushuai tomeasure@foxmail.com 2018/01/16

# I'll use these libraries
from numpy import random, array, tile, concatenate, save, sqrt, square
from numpy import round as nround
from numpy import sum as nsum
from shutil import move
from os import mkdir
# set number and dimension of the data set
number_of_each_label = 250
dimension = 10
# set expectation (int) & variance of each value of features for each label by Gaussian Distribution
u_1 = random.randn(dimension); sigma_1 = 3
u_2 = random.randn(dimension); sigma_2 = 3
u_1.dtype = 'int'; u_1 %= 20
u_2.dtype = 'int'; u_2 %= 20
# generate features
#     initial features with N(0, 1)
#     change variance
#     change expectation
#     take first two numbers after decimal point as significant digits
features_1 = random.randn(number_of_each_label, dimension)
features_2 = random.randn(number_of_each_label, dimension)
features_1 *= sigma_1; features_1 += u_1;
features_2 *= sigma_2; features_2 += u_2
features_1 = nround(features_1, 2)
features_2 = nround(features_2, 2)
# generate labels
labels_1 = array(1)
labels_2 = array(0)
labels_1 = tile(labels_1, (number_of_each_label, 1))
labels_2 = tile(labels_2, (number_of_each_label, 1))
# merge features and labels
data_1 = concatenate((features_1, labels_1), axis=1)
data_2 = concatenate((features_2, labels_2), axis=1)
data = concatenate((data_1, data_2))
# restore these data into data.csv
save("data.npy", data)
# move the file data.npy into ../data/
try:
    mkdir('../data/')
except:
    move('./data.npy', '../data/data.npy')
    pass
else:
    move('./data.npy', '../data/data.npy')
# print information of these data
print("--------------------------------------------------")
print("u_1: ", u_1, " sigma_1: ", sigma_1)
print("u_2: ", u_2, " sigma_2: ", sigma_2)
dist = sqrt(nsum(square(u_1 - u_2)))
print("the distance between u_1 and u_2: ", dist)
print("--------------------------------------------------")
