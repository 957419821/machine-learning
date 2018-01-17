import time
def Start():
    return time.time()
def End():
    return time.time()
def time_used(s, e, mode):
    used = int(e - s)
    second = used % 60
    minutes = used // 60
    minute = minutes % 60
    hour = minutes // 60
    print("--------------------------------------------------")
    print("the used time is: ", hour, " hours ", minute, " minutes ", second, " second mode:", mode)
    print("--------------------------------------------------")
