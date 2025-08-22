#Funtions (OPERATIONS +*-/)
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    if b!=0:
        return a/b
    else:
        return "Error: Division by 0"
    


while(True):
    num1=float(input("Enter the first  number"))
    num2=float(input("Enter the second number"))

    print("Choose operation: 1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = int(input(("Enter choice: ")))

    if choice==1:
        print("Result : ",addition(num1,num2))
    elif choice==2:
        print("Result : ",subtraction(num1,num2))
    elif choice==3:
        print("Result : ",Multiplication(num1,num2))
    elif choice==4:
        print("Result : ",Division(num1,num2))
    elif choice==5:
        print("Exiting... Bye!!")
        break

    else:
        print("INVALID CHOICE!!!!")
    print("-"*30)
