#prime number different logic
num = 9
if num <= 1:
    print(f'{num} is not prime number')
else:
    for val in range(2,num):
        if num % val == 0:
            print(f'{num} is not prime number')
            break
    else:
        print(f'{num} is a prime number')
