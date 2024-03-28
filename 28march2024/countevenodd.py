# count number of even and odd integers in an array 
def countEvenOdd(arr):
    even=0
    odd=0
    for ele in arr:
        if ele%2==0:
            even+=1
        else:
            odd+=1
    print(even,odd)

arr=[1,2,3,4,5]
countEvenOdd(arr)