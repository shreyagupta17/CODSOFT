print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")
option=int(input("Choose operation:"))

if(option in [1,2,3,4]):
    if(option==1):
        num1=int(input("enter first number:"))
        num2=int(input("enter second number:"))
        result=num1+num2
    elif(option==2):
        num1=int(input("enter first number:"))
        num2=int(input("enter second number:"))
        result=num1-num2
    elif(option==3):
        num1=int(input("enter first number:"))
        num2=int(input("enter second number:"))
        result=num1*num2
    elif(option==4):
        num1=int(input("enter first number:"))
        num2=int(input("enter second number:"))
        result=num1/num2
print("The result is :",result)

