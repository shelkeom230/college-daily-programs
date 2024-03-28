# in one line 
def sortArr(arr):
    print(sorted(arr[:len(arr)//2]),sorted(arr[len(arr)//2:],reverse=True))

n=int(input("enter array size: "))
arr=[]

for i in range(n):
    arr.append(int(input()))
sortArr(arr)