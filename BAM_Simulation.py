import numpy as np
import random
import Image
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
w = x.T.dot(t)
print(w)

print("Give an input pattern")

pattern = np.array([0,0,1,1])
print(pattern)

print(pattern.dot(w))

rev_pattern = np.array([2,1])
print(rev_pattern.dot(w.T))

#Damn , Forgot to apply activation functions