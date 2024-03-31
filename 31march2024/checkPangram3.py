# using set 
def checkPangram(string):
    return len(set(string.lower().replace(" ","")))==26

print(checkPangram('omkar shelke'))