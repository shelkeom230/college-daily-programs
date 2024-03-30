# remove duplicates from the array 
def removeDuplicate(arr):
    return list(set(arr))

def remove2(arr):
    unique_arr = []
    for ele in arr:
        if arr.count(ele) == 1:
            unique_arr.append(ele)
    return unique_arr


arr=[1,2,3,4,5,1,2]
result=removeDuplicate(arr)
result2=remove2(arr)
# print(result)
print(result2)