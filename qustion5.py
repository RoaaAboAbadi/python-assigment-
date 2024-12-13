# Write a Python function to print the even numbers from a given list 

myList =[1,2,3,4,5,6,7,8]
def evenNumber (list):
    for i in list:
        if i % 2 == 0:
            print(i)
evenNumber(myList)