# WRITE A PROGRAM IN PYTHON TO FIND THE NUMBER GREATEST AMONG THREE NUMBERS

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a>b and a>c:
    print(f"{a} is the greatest")
elif b>a and b>c:
    print(f"{b} is the greatest")
elif c>a and c>b:
    print(f"{c} is the greatest")