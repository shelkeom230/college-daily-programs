# 18. How to calculate the number of vowels and consonants in a string?
def cal(string):
    vowels=0
    consonants=0
    vowels_set=['a','e','i','o','u']
    for ele in string:
        if ele in vowels_set:
            vowels+=1
        else:
            consonants+=1
    print(f"vowels: {vowels},consonants: {consonants}")

string="omkar shelke"
cal(string)