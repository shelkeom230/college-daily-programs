# using indexing 
def rotateArray(arr,k):
    if len(arr)<=1:
        return arr 
    else:
        k=k%len(arr)
        return arr[-k:]+arr[:-k]

arr=[1,2,3,4,5]
rotated=rotateArray(arr,2)
print(rotated)