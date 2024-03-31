from collections import deque
def rotateArr(arr,k):
    if len(arr)<=1:
        return arr 
    else:
        k=k%len(arr)
        return arr[-k:]+arr[:-k]

print(rotateArr([1,2,3,4,5],3))