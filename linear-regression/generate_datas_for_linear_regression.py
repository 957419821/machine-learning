import random as rand
import math

def linear_function(coefs, args):
    """
       len(coefs) == len(args) + 1 
    """
    sigma = 3
    dataType = str(type(args))[8:-2]
    # if args is a number, use the formula: y=ax+b
    if dataType=="int" or dataType=="float":
        noise = math.floor(100 * rand.gauss(0, sigma)) / 100
        return coefs[0] * args + coefs[1] + noise
    # if args is a tuple/list, use the formula: y=a1x+a2x+...+anx+b
    val = 0
    for i in range(len(args)):
        val += coefs[i] * args[i]
    val += coefs[len(coefs)-1] 
    # add noise
    noise = math.floor(100 * rand.gauss(0,sigma)) / 100
    val += noise
    return val

def generator(func, coefs, args):
    datas = ""
    for i in range(len(args)):
        data = str(args[i]) + ',' + str(func(coefs, args[i])) + '\n'
        datas += data
    fout = open("datas.txt", "wt")
    fout.write(datas)
    fout.close()

coefs = [2, 1]
samples_number = 100
args = [i+1 for i in range(samples_number)]
func = linear_function
generator(func, coefs, args)
