#prime number or not
num = 7
fact_count = 0
for val in range(1,num+1):
    if num % val == 0:
        fact_count += 1
if fact_count == 2:
    print(f'{num} is prime number')
else:
    prime(f'{num} is not prime number')

