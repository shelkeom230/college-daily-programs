# using list comprehension 
def printUnique(arr):
    print([ele for ele in arr if arr.count(ele)==1])

printUnique([1,2,3,3,4,4,5,6,7,8])