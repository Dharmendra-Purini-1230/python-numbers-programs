#least factor among 2,3,5,7 given numbers
num = 30
if num % 2 == 0:
    print(f'{num} is divisible by 2')
elif num % 3 == 0:
    print(f'{num} is divisible by 3')
elif num % 5 == 0:
    print(f'{num} is divisible by 5')
elif num % 7 == 0:
    print(f'{num} is divisible by 7')
else:
    print('no factor')
