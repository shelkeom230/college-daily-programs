# using list comprehension and sum functoin 
def countEvenOdd(arr):
    even,odd=sum(1 for ele in arr if ele%2==0),sum(1 for ele in arr if ele%2!=0)
    print(even,odd)

arr=[1,2,3,4,5]
countEvenOdd(arr)