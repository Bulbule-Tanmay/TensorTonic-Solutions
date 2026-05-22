import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # out = []
    # for i in x:
    #     out.append(1/(1+math.exp(-i)))
    y = np.array(x);
    y =  1/(1+np.exp(-y))
    return y
    pass