# rotate array elements by 1 position 
def rotateArrElements(arr):
    if len(arr)<=1:
        return arr
    else:
        return arr[1:]+arr[:1]
arr=[1,2,3,4,5]
rotated=rotateArrElements(arr)
print(rotated)