# using temp variable  
def rotateArray(arr):
    if len(arr)<=1:
        return arr 
    else:
        first=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1]=first
    return arr 

arr=[1,2,3,4,5]
rotated=rotateArray(arr)
print(rotated)
