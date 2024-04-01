# 20. Write a program to find a word in a given string that has the highest number of repeated letters. If not found, return -1.

def find(string):
    words=string.split(' ')

    max_repeated_count=0
    word_with_max_repeated=None 

    for word in words:
        count_chars={}
        for char in word:
            if char in count_chars:
                count_chars[char]+=1
            else:
                count_chars[char]=1
    
    # find max count of repeted letters 
        max_count=max(count_chars.values(),default=0)

        if max_count>max_repeated_count:
            max_repeated_count=max_count
            word_with_max_repeated=word 

    if word_with_max_repeated:
        return word_with_max_repeated
    else:
        return -1 

string = "omkar google"
result = find(string)
print("Word with highest repeated letters:", result)
       