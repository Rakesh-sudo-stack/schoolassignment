# WRITE A PROGRAM IN PYTHON TO FIND THE PRIME NUMBER

num = int(input("Enter any number: "))

if num > 1:
    if num==2:
        print(f"{num} is a prime number")
    else:
        for j in range(2,num):
            if num%j == 0:
                print(f"{num} is not a prime number")
                break
            elif j == num - 1 and num % j != 0:
                print(f"{num} is a prime number")