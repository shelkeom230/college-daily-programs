# using iteration 
def findFib(n):
    if n<=1:
        return n
    else:
        fib_values=[0,1]
        for i in range(2,n+1):
            fib_values.append(fib_values[i-1]+fib_values[i-2])
        return fib_values[n]

n=int(input())
print(findFib(n))
