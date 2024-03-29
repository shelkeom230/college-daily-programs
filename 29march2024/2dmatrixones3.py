# using itertools
import itertools

def maxOnes(matrix):
    max_row_index, _ =max(enumerate(matrix),key=lambda x:sum(x[1]))
    return max_row_index

matrix=[
    [1,0,0,1],
    [1,1,1,1],
    [0,0,1,1],
    [1,0,0,0]
]
print(maxOnes(matrix))