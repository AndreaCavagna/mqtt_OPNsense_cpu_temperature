import numpy as np


def running_mean(x, N, array):
    array.pop(0)
    array.append(x)
    return (np.sum(array)) / float(N)