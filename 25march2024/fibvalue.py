# using recursion 
def findFib(n):
    if n<=1:
        return n
    else:
        return findFib(n-1)+findFib(n-2)

n=int(input())
print(findFib(n))