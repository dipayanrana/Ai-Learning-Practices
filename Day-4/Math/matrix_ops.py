import numpy as np  

def multiply_matrices(m1, m2):  
    return np.dot(m1, m2)  

def is_multipliable(m1, m2):  
    return m1.shape[1] == m2.shape[0]  