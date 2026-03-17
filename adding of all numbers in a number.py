#write a program to add all digits in a number?
num = 345
dup = num
total = 0
while num > 0:
    rem = num % 10
    total = total + rem
    num = num // 10
print(f'sum of all digits in {dup} is {total}')
