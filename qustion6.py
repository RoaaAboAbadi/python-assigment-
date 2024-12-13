# Write a Python function to multiply all the numbers in a list 

myList =[1,2,3,4,5,6]

def multiplyNumbers (list):
    result =1
    for i in list:
        result *=i
    return result

print(multiplyNumbers(myList))