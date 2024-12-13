#  Write a Python program to sum all the odd  items in a list 

myList =[1,2,3,4,5,6]
sum=0
for i in myList:
    if i%2 !=0:
        sum+=i
print(sum)