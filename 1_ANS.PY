# WRITE A PROGRAM IN PYTHON TO FIND A BUZZ NUMBER

print("\t\t BUZZ NUMBER IS CHECKED FOR 7")

num = int(input("Enter any no: "))

if num%7 == 0 or num % 10 == 7:
    print(f"{num} is a buzz number")
else:
    print(f"{num} is not a buzz number")