import numpy as np
import random
import os, subprocess


# Take specific input X which is of 4X4 matrix

x = np.array([[1,0,1,0],[1,0,0,1],[1,1,0,0],[0,0,1,1]],np.int32)
print(x)
print("check")

# Take specific output vector T which is of 4X2 matrix

t = np.array([[1,0],[1,0],[0,1],[0,1]])
print(t)

# Initialise weight matrix of size(4,2) to 0f
w = np.zeros(shape = (4,2))
print("weight matrix is ")
print(w)

print(x.T.dot(t))

