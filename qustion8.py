# text ="the program is running fast"
text = input("Enter a text:")
newText = text.split()

def wordLength (dic):
    newDic ={}
    for word in dic:
        newDic[word] = len(word)
    return newDic

print(wordLength(newText))