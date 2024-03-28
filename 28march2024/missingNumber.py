# find missing number in an array using set difference 
def find_missing_numbers(arr):
    min_num=min(arr)
    max_num=max(arr)
    all_numbers=set(range(min_num,max_num+1))
    missing=list(all_numbers-set(arr))
    return missing



arr = [1, 2, 3, 5, 9]
missing_numbers = find_missing_numbers(arr)
print(missing_numbers)
