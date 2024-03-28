# usign list comprehension 
def commonEle(arr1,arr2):
    print([ele for ele in arr1 if ele in arr2])

arr1=[1,2,3,4]
arr2=[2,3,11,222]
commonEle(arr1,arr2)