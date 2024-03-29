# 2D matrix question - Find row with maximum no. of 1’s
def findRows(matrix):
    max_ones=max(matrix,key=lambda x:x.count(1))
    return matrix.index(max_ones) 

matrix = [
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 1]
]
print(findRows(matrix))