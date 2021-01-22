'''
Write a program that accepts any number of digits from the user - enter a digit, press enter, followed by another digit.
Once the user is done with entering the numbers - press Enter
Followed by the arithmetic operation that should be performed on the digits entered 
'''

import re
count =0
number=[]

a = input("Enter the number- Enter to exit:")

while a!="":
    number.append(a)
    a = input("Enter the number - Enter to exit:")
operation = input("Enter the Operation")

if re.search('addition|add',operation.lower()):
    for i in number:
        count = count + float(i)
    print("Sum of the number is", count)

elif re.search('substraction|substract',operation.lower()):
    for i in number:
        count = count - float(i)
    print("Result of substraction is", count)

elif re.search('multiplcation|multiply',operation.lower()):
    mult =1
    for i in number:
        mult =  mult * float(i)
    print("Result of multiplication is", mult)
#handle division by 0
elif re.search('division|divide',operation.lower()):
    try:
        a = []
        x = 1
        while x < len(number):
            a.append(x)
            x=x+1
            div = float(number[0])
        for l in a:
            div = div/float(number[l])
        print("The result of division is", div)
    except ZeroDivisionError:
        print("Cannot divide by zero; check the numbers and re-enter")
else:
    print("Enter a valid operation - Addition, Substraction, Multiplication or Division")
