# sort first half in ascending order and later in descending order 
def sortArr(arr):
    n=len(arr)
    first=[]
    second=[]

    mid=n//2

    for i in range(mid):
        first.append(arr[i])
    
    for j in range(mid,n):
        second.append(arr[j])
    
    first.sort()
    second.sort(reverse=True)
    print(first,second)

arr=[]
n=int(input("enter size of array: "))
for i in range(n):
    arr.append(int(input()))
sortArr(arr)
