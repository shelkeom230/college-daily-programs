# using pop method 
def rotateArray(arr,k):
    if len(arr)<=1:
        return arr 
    else:
        k=k%len(arr)
        for _ in range(k):
            arr.insert(0,arr.pop())
    return arr 
arr=[1,2,3,4,5,6,7,8,9,10]
rotated=rotateArray(arr,4)
print(rotated)