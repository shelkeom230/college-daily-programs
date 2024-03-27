# reverse the array 
def reverseArr(arr):
    return arr.reverse()

n=int(input("enter array size: "))
arr=[]
for i in range(n):
    arr.append(int(input()))

reverseArr(arr)
print(arr)