# Grading System

n=input("Please enter your name: ")
g=int(input("Enter your marks out of 100: "))
if g>90 and g<=100:
    print(f"{n} Your Grade is A+")
elif g>80 and g<=90:
    print(f"{n} Your Grade is A")
elif g>70 and g<=80:
    print(f"{n} Your Grade is B+")
elif g>60 and g<=70:
    print(f"{n} Your Grade is B")
elif g>50 and g<=60:
    print(f"{n} Your Grade is C+")
elif g>=40 and g<=50:
    print(f"{n} Your Grade is C")
elif g<40:
    print(f"{n} Your Grade is F , Fail")
elif g>100 or g<0:
    print("!Invalid Input!")