# get train and valid set with mode
def initial_data_train_valid(data, tv, mode):
    if mode == 'hold_out':
        data_train, data_valid = tv.hold_out(data)
    elif mode[0:-2] == 'cross_validation':
        data_train, data_valid = tv.cross_validation(data, int(mode[-1]))
    elif mode == 'bootstrapping':
        data_train, data_valid = tv.bootstrapping(data)
    x_train = data_train[:, 0:-1]; y_train = data_train[:, -1]
    x_valid = data_valid[:, 0:-1]; y_valid = data_valid[:, -1]
    return x_train, y_train, x_valid, y_valid
