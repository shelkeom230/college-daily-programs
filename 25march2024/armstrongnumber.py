# check for armstrong number 
def checkArmstrong(n):
    copyn=n 

    sum=0
    while n>0:
        digit=n%10
        sum+=pow(digit,3)
        n//=10
    
    if sum==copyn:
        print(f"{copyn} is an armstrong number")
    else:
        print(f"{copyn} is not an armstrong number")


n=int(input())
checkArmstrong(n)


