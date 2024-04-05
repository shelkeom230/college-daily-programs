
# Write a Java program to take the last three characters from a given string. It will add the three characters at both the front and back of the string. String length must be greater than three and more.

# Test data: "Python" 
# Sample Output: honPythonhon

def result(string):
    lastThree=string[-3:]
    result=lastThree+string+lastThree
    return result


string=input("enter a string: ")
print(result(string))
