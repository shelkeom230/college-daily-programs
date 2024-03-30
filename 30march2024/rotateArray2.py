# rotate array elements to left by 1 position 
def rotateArray(arr):
    if len(arr)<=1:
        return arr
    else:
        first_element=arr.pop(0)
        arr.append(first_element)
    return arr 

arr=[1,2,3,4]
rotated=rotateArray(arr)
print(rotated)