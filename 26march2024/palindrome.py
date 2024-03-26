# number is palindrome or not 
def checkPalindrome(n):
    print('yes' if str(n)==str(n)[::-1] else 'no')

def checkPal(n):
    revnum=str(n)[::-1]
    if str(n)==revnum:
        print('yes')
    else:
        print('no')   
n=int(input())
# checkPalindrome(n)
checkPal(n)