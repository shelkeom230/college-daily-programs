# using for loop 
def revArr(arr):
    rev_arr=[]
    for i in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[i])
    print(rev_arr)

arr=[1,2,3,4]
revArr(arr)
