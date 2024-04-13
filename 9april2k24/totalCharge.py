# Problem Statement – In an airport , the Airport authority decides to charge some minimum amount to the passengers who are carrying luggage with them. They set a threshold weight value, say T, if the luggage exceeds the weight threshold you should pay double the base amount. If it is less than or equal to the threshold then you have to pay $1.
# Returns: The function must return an INTEGER denoting the required amount to be paid.

# The first line contains an integer, N, denoting the number of luggages.
# Each line i of the N subsequent lines (where 0 <= i < n) contains an integer describing weight of ith luggage.
# The next line contains an integer, T, denoting the threshold weight of the boundary wall.

def returnAmount(n,weights,boundaryVal):
    amount=0
    for ele in weights:
       if ele>boundaryVal:
           amount+=2
       else:
           amount+=1
    return amount           

n=int(input("enter number of luggages: "))
weights=[]
for i in range(n):
    weights.append(int(input()))
boundaryVal=int(input("enter the boundary value for weights: "))    
result=returnAmount(n,weights,boundaryVal)
print(result)                