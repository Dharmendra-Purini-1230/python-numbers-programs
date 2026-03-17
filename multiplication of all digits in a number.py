#write program o multiply all digits in numbeer
num = 345
dup = num
total = 1
while num > 0:
    rem = num % 10
    total = total * rem
    num = num // 10
print(f'multiplication of all  digits in {dup} is {total}')
    
