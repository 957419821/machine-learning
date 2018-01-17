##### 这个文件夹中存放有三个模块：time_used.py，train_valid.py，update_coef.py</br>
###### time_used.py 用于计算程序运行的时间，包含三个函数：Start、End、time_used(s,e)：
* 第一个函数用于记录程序开始时的绝对时间
* 第二个函数用于记录程序结束时的时间
* 第三个函数用于输出程序的运行时间
###### train_valid.py 中包含了一个类，该类拥有：
* 两个属性分别用于记录留出法的比率和交叉验证的折数，相应的默认值是0.8和10
* 三个方法从给定的数据获取训练集和验证集，分别采用留出法、k折交叉验证法、自主法
###### update_coef.py 包含一个用来更新权重和偏差的函数