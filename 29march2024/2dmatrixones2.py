# using numpy 
import numpy as np 
def findOnes(matrix):
    ones_count=np.sum(matrix,axis=1)
    return np.argmax(ones_count)

matrix=[
    [1,0,0,1],
    [1,1,1,1],
    [0,0,1,1],
    [1,0,0,0]
]
print(findOnes(matrix))