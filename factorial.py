num = int(input('enter the nuber:'))
factorial = 1
if num > 0:
    for val in range(1,num+1):
        factorial = val * factorial
    print(f'factorial of {num} is {factorial}')
else:
    print('factorial is not possible')
        
        
