#Write a Python program to get unique values from a list
myList =[1,2,3,3,4]


newList =[]
for i in myList:
    if i not in newList:
        newList.append(i)
        print(i)

# Another simple solution        
# uniqeValues =set(myList)
# print(uniqeValues)
