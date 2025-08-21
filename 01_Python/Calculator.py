#Mayank's First Project - Basic Calculator 

#Take input from the user
num1=float(input(("Enter first number  :  ")))
num2=float(input(("Enter second number :  ")))


#here the operations choices 
print("Enter according to your choice 1/2/3/4")
print("1 for Addition")
print("2 for Subtraction")
print("3 for multiplication")
print("4 for Division")


choice=input("enter your choice from 1/2/3/4:  ")


#calculate result

if choice=='1':
    print("Result = ",num1+num2)
elif choice=="2":
    print("Result =",num1-num2)
elif choice=="3":
    print("Result =",num1*num2)
elif choice=="4":
    if num2!=0:
        print("Result =",num1/num2)
    else:
        print("ERROR: Division by 0 ")
else:
    print("INVALID CHOICE!!!")