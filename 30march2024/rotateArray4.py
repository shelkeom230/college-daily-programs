# rotate array using collections.deque 
from collections import deque
def rotateArray(arr):
    if len(arr)<=1:
        return arr 
    else:
        dq=deque(arr)
        dq.rotate(-1)
        return list(dq) 

arr=[1,2,3,4,5]
rotated=rotateArray(arr)
print(rotated)