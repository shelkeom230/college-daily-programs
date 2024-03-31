# 17. Program to check number Armstrong or not.
def checkArmstrong(number):
    sum=0
    copyn=number

    while number>=1:
        digit=number%10
        sum+=pow(digit,3)
        number//=10
    
    if copyn==sum:
        print('armstrong number')
    else:
        print('not armstrong number')

n=int(input("enter a number: "))
checkArmstrong(n)