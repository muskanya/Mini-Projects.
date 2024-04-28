# Basic Calculator

a=int(input("Enter the first number: "))

b=int(input("Enter the second number: "))

choice=input("Select which operation you want to perform! (+,-,*,/,//,%,^): ")

if choice=="+":
    print("\nThe Addition of", a,"+",b,"is:",a+b)

elif choice=="-":
    print("\nThe Subtraction of",a,"-",b,"is:",a-b)

elif choice=="*":
    print("\nThe Multiplication of",a,"*",b,"is:",a*b)

elif choice=="/":
    print("\nThe Division of",a,"/",b,"is:",a/b)

elif choice=="//":
    print("\nThe Division(Round off) of",a,"//",b,"is:",a//b)

elif choice=="%":
    print("\nThe Reminder of",a,"%",b,"is:",a%b)

elif choice=="^":
    print("\nThe Exponential of",a,"^",b,"is:",a**b,"\n")

else:
    print("Invalid Character")