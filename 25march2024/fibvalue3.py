#using memoization (dp)
def fibMemo(n,memo={}):
    if n in memo:
        return memo[n]
    elif n<=1:
        return n 
    else:
        return fibMemo(n-1,memo)+fibMemo(n-2,memo)

n=int(input())
print(fibMemo(n))