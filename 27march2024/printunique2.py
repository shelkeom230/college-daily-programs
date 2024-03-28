# using dict 
def printUnique(arr):
    unique_num={}

    for ele in arr:
        unique_num[ele]=unique_num.get(ele,0)+1

    unique=[]
    for num,count in unique_num.items():
        if count==1:
            unique.append(num)
    print(unique)   
arr=[1,1,2,3,3,3,4]
printUnique(arr)