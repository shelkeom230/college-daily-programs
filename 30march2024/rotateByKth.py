# rotate array element by kth position
from collections import deque 
def rotateArray(arr,k):
    if len(arr)<=1:
        return arr 
    else:
        k=k%len(arr)
        dq=deque(arr)
        dq.rotate(-k)
        return list(dq)

arr=[1,2,3,4,5]
rotated=rotateArray(arr,2)
print(rotated)
