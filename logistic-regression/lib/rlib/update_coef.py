# used by ../logistic_regression.py to update weights and bias
#     the type of w is np.ndarray
#     b is a scale
#     plpw and plpb are derivatives of loss function
#     alpha has the learning rate of w and b: (lr_w, lr_b)
#     loss function is ylnh+(1-y)ln(1-h)
#     I'll use Stochastic Gradient Descent to update coef
def update_weights_bias_SGD(x, y, w, b, alpha, sigmoid):
    new_w = w; new_b = b; alpha_w, alpha_b = alpha
    for i in range(len(x)):
        hi = sigmoid(x[i], w, b)
        new_w += alpha_w * x[i] * (y[i] - hi)
        new_b += alpha_b * (y[i] - hi)
    return new_w, new_b
