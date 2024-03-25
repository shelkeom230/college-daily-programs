# bubble sort without temp 
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[]
length=int(input("enter length of array: "))

for i in range(length):
    arr.append(int(input()))

bubbleSort(arr)
print(arr)
