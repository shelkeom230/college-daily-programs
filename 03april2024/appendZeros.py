# append all zeros at the end of the list 
def appendzeros(arr):
    zeros_count=arr.count(0)
    arr=[ele for ele in arr if ele!=0]
    arr.extend([0]*zeros_count)
    return arr 

def appendZeros2(arr):
    arr_count=arr.count(0)
    for ele in range(arr_count):
        arr.remove(0)
    arr.extend([0]*arr_count)
    return arr 

arr=[1,2,3,4,0,0,2,3,0]
result=appendzeros(arr)
print(result)