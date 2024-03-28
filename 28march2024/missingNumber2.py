# traditional approach using sum and difference 
def missingNumber(arr):
    n=len(arr)+1
    total_sum=n*(n+1)//2
    arr_sum=sum(arr)
    missing_sum=total_sum-arr_sum

    missing_numbers = []
    for i in range(1,n):
        missing_candidate=i+missing_sum
        if missing_candidate not in arr and 1<=missing_candidate<=n:
            missing_numbers.append(missing_candidate)

    return missing_numbers

arr=[1, 2, 3, 5, 7]
print(missingNumber(arr))