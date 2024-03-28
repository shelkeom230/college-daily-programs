# number is palindrome or not 
def checkPalindrome(n):
    print('yes' if str(n)==str(n)[::-1] else 'no')

def checkPal(n):
    rev_num=str(n)[::-1]

    if rev_num==str(n):
        print('yes')
    else:
        print('no')   
n=int(input())
# checkPalindrome(n)
checkPal(n)