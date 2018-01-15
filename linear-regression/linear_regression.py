# Author Liushuai tomeasure@foxmail.com

# Batch Gradient Descent
def update_weight_bias_BGD(x, y, w, b, alpha):
    pfpw = 0; pfpb = 0; m = len(x); alpha_w, alpha_b = alpha
    for i in range(len(x)):
        pfpw += x[i] * (w * x[i] + b - y[i])
        pfpb += w * x[i] + b - y[i]
    pfpw /= m; pfpb /= m
    new_w = w - alpha_w * pfpw; new_b = b - alpha_b * pfpb
    return new_w, new_b
# Stochastic Gradient Descent
def update_weight_bias_SGD(x, y, w, b, alpha):
    new_w = w; new_b = b; alpha_w, alpha_b = alpha
    for i in range(len(x)):
        new_w -= alpha_w * x[i] * (new_w * x[i] + new_b - y[i])
        new_b -= alpha_b * (new_w * x[i] + new_b - y[i])
    return new_w, new_b
# Mini-batch Gradient Descent
def update_weight_bias_MBGD(x, y, w, b, alpha):
    batch_size = 3; i = 0
    new_w = w; new_b = b; alpha_w, alpha_b = alpha
    while i < len(x):
        pfpw = 0; pfpb = 0
        for j in range(i,i+batch_size):
            if(j < len(x)):
                pfpw += x[i] * (new_w * x[i] + new_b - y[i])
                pfpb += new_w * x[i] + new_b - y[i]
            else:
                i = len(x)
                break
        pfpw /= batch_size; pfpb /= batch_size
        new_w -= alpha_w * pfpw; new_b -= alpha_b * pfpb
        i += batch_size
    return new_w, new_b
# Sum of Squared Error
def SSE(x, y, w, b):
    sse = 0; m = len(x)
    for i in range(m):
        differ = w * x[i] + b - y[i]
        square_differ = differ ** 2
        sse += square_differ
    sse /= m * 2
    return sse
# linear regression
def linear_regression(w_b_tuple):
    from getDatasFromTxt import getXY
    X, Y = getXY()
    alpha = (0.0001, 0.001)
    loop_times = 20000
    # test BGD
    w, b = w_b_tuple
    for i in range(loop_times):
        w, b = update_weight_bias_BGD(X, Y, w, b, alpha)
    SSE_BGD = SSE(X, Y, w, b); w_BGD = w; b_BGD = b
    # test SGD
    w, b = w_b_tuple
    for i in range(loop_times):
        w, b = update_weight_bias_SGD(X, Y, w, b, alpha)
    SSE_SGD = SSE(X, Y, w, b); w_SGD = w; b_SGD = b
    # test MBGD
    w, b = w_b_tuple
    for i in range(loop_times):
        w, b = update_weight_bias_MBGD(X, Y, w, b, alpha)
    SSE_MBGD = SSE(X, Y, w, b); w_MBGD = w; b_MBGD = b
    # print weight and bias
    print("weight: ", w_BGD, " bias: ", b_BGD, " SSE: ", SSE_BGD, " by BGD")
    print("weight: ", w_SGD, " bias: ", b_SGD, " SSE: ", SSE_SGD, " by SGD")
    print("weight: ", w_MBGD, " bias: ", b_MBGD, " SSE: ", SSE_MBGD, " by MBGD")
