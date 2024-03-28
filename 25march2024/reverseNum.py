def revNum(n):
    rev_num=int(str(n)[::-1])
    print(f"reverse of {n} is {rev_num}")

n=int(input("enter a number: "))
revNum(n)