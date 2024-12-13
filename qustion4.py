# Write a Python function to find the Max of three numbers 

def maxNumber (num1, num2, num3):
    result =0
    if num1 > num2 and num1 > num3:
        result = num1
    elif num2 > num3 and num2 > num1:
        result = num2
    else:
        result = num3
    return result
print(maxNumber(3, 8, 9))