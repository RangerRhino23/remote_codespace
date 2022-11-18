import random

def addition():
    num1 = random.randint(0,12)
    num2 = random.randint(0,12)
    sum = int(num1+num2)
    print(num1,"+",num2,"= ?")
    answer = int(input())
    if answer == sum:
        print("Correct!")
        addition()
    elif answer != sum:
        print("Incorrect, the answer was", sum)
        addition()
    elif answer == 'end':
        quit()
    else:
        print("Error")
        addition()

def subtraction():
    num1 = random.randint(0,12)
    num2 = random.randint(0,12)
    sum = int(num1-num2)
    print(num1,"-",num2,"= ?")
    answer = int(input())
    if answer == sum:
        print("Correct!")
        subtraction()
    elif answer != sum:
        print("Incorrect, the answer was", sum)
        subtraction()
    elif answer == 'end':
        quit()
    else:
        print("Error")
        subtraction()

def multiplication():
    num1 = random.randint(0,12)
    num2 = random.randint(0,12)
    sum = int(num1*num2)
    print(num1,"x",num2,"= ?")
    answer = int(input())
    if answer == sum:
        print("Correct!")
        multiplication()
    elif answer != sum:
        print("Incorrect, the answer was", sum)
        multiplication()
    elif answer == 'end':
        quit()
    elif answer == 'end':
        quit()
    else:
        print("Error")
        multiplication()

def division():
    num1 = random.randint(0,12)
    num2 = random.randint(0,12)
    sum = int(num1/num2)
    print(num1,"/",num2,"= ?")
    answer = int(input())
    if answer == sum:
        print("Correct!")
        division()
    elif answer != sum:
        print("Incorrect, the answer was", sum)
        division()
    elif answer == 'end':
        quit()
    else:
        print("Error")
        division()

option = input("What math facts do you want to practice? (Add,Sub,Mul,Div) ")
option = option.lower()
if option == 'add':
    addition()
elif option == 'sub':
    subtraction()
elif option == 'mul':
    multiplication()
elif option == "div":
    division()
else:
    print("Error, please try again")