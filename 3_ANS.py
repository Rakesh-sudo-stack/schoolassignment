# WRITE A PROGRAM IN PYTHON TO FIND THE FIRST 10 PRIME NUMBERS

primenums = [2]

i = 1

while True:
    if i > 2:
        for j in range(2,i):
            if i%j == 0:
                break
            elif j == i - 1 and i % j != 0:
                primenums.append(i)
    i = i+1
    if len(primenums) == 10:
        break

for val in primenums:
    print(val)