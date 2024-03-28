# using set and set_intersectoin method 
def commonEle(arr1,arr2):
    set1=set(arr1)
    set2=set(arr2)

    print(list(set1.intersection(set2)))

arr1=[1,2,3,4]
arr2=[5,6,1,2]
commonEle(arr1,arr2)