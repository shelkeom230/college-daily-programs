# sort first half in ascending order and later in descending order 
def sortArr(arr):
    n=len(arr)
    first=[]
    second=[]
    start=0
    end=n 

    mid=len(arr)//2
    for i in range(mid):
        first.append(arr[i])
    
    for i in range(mid,n):
        second.append(arr[i])
    
    first.sort()
    second.sort(reverse=True)
    print(first,second)

arr=[]
n=int(input("enter size of array: "))
for i in range(n):
    arr.append(int(input()))
sortArr(arr)
