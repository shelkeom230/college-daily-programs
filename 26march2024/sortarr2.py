def sortArr(arr):
    mid=len(arr)//2
    first=sorted(arr[:mid])
    second=sorted(arr[mid:],reverse=True)
    print(first,second)

n=int(input("enter array size: "))
arr=[]
for i in range(n):
    arr.append(int(input()))

sortArr(arr)