# print fib value upto n using recursion 
def printFib(n):
    fib_values=[]
    for i in range(n):
        fib_values.append(Fib(i))
    return fib_values

def Fib(n):
    if n<=1:
        return n 
    else:
        return Fib(n-1)+Fib(n-2)
n=int(input())
print(printFib(n))