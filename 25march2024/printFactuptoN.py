def findFact(n):
    if n==0:
        return 1
    return n*findFact(n-1)

def printFact(n):
    fact_values=[]
    for i in range(n):
        fact_values.append(findFact(i))
    return fact_values

n=int(input())
print(printFact(n))