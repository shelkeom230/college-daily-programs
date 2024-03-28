# find common elements between two array 
def findCommon(arr1,arr2):
    common=[]
    for ele in arr1:
        if ele in arr2:
            common.append(ele)
    print(common)

arr1=[1,2,3,4,5]
arr2=[2,3,5,6,7]
findCommon(arr1,arr2)
