# using while loop 
def revArr(arr):
    i=len(arr)-1
    revarr=[]
    while i>=0:
        revarr.append(arr[i])
        i-=1
    print(revarr)

arr=[1,2,3]
revArr(arr)