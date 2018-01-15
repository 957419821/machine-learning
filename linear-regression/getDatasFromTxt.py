def getXY():
    filename = 'datas.txt'
    fin = open(filename)
    datas = fin.read()
    fin.close()
    datas = datas.split('\n')
    del datas[-1]
    for i in range(len(datas)):
        datas[i] = datas[i].split(',')
        datas[i][0] = float(datas[i][0])
        datas[i][1] = float(datas[i][1])
    x = []; y = []
    for data in datas:
        x.append(data[0])
        y.append(data[1])
    return x,y
