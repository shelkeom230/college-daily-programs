# reverse using temp var 
def revArr(arr):
    rev_arr=[]
    for i in arr:
        rev_arr.insert(0,i)
    print(rev_arr)

arr=[1,2,3,4]
revArr(arr)