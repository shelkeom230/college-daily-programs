# bubble sort using temp variable 
def bubbleSort(arr):
    n=len(arr)

    temp=0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp 


arr=[]
length=int(input("enter array size: "))
for i in range(length):
    arr.append(int(input()))
bubbleSort(arr)
print(arr)
