def printArmstrong(n):
    armstrong_numbers = []
    for i in range(n):
        if isArmstrong(i):
            armstrong_numbers.append(i)
    return armstrong_numbers

def isArmstrong(n):
    len_number=len(str(n))
    original_num=n 
    sum=0

    while n>0:
        digit=n%10
        sum+=digit**len_number
        n//=10
    
    return sum==original_num



# Example usage:
n = int(input())
armstrong_numbers = printArmstrong(n)
print("Armstrong numbers up to", n, "are:", armstrong_numbers)
