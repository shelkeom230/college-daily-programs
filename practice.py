def countEvenOrOdd(arr):
    even=0
    odd=0

    for ele in arr:
        if ele%2==0:
            even+=1
        else:
            odd+=1
    print(even,odd)

countEvenOrOdd([1,1,2,3,4,4,5])