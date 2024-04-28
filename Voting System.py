# Voting System

print("Namaste! Welcome to Voting System")
name=input("Please Enter your name: ")
age=int(input("Enter your age: "))

if age>=18:
    print("Verified! You can vote.")
    while True:
        vote=input('''Please select which political party you want to vote\n
        Below is the list of available Political Parties:-
        \n1).BJP\n2).AAP\n3).BSP\n4).CPI(M)\n5).INC\n6).NPP\n
        Please enter the name of the Political Party here: ''').upper()

        if vote=="BJP":
            print(f"Thank You! You have voted {vote}")

        elif vote=="AAP":
            print(f"Thank You! You have voted {vote}")

        elif vote =="BSP":
            print(f"Thank You! You have voted {vote}")

        elif vote=="CPI(M)":
            print(f"Thank You! You have voted {vote}")

        elif vote=="INC":
            print(f"Thank You! You have voted {vote}")

        elif vote=="NPP":
            print(f"Thank You! You have voted {vote}")

        else:
            print("Wrong choice")
            continue
        break

else:
    print("You are not eligible to vote")

feed=input("Please enter your feedback: ")
print("Thank You")