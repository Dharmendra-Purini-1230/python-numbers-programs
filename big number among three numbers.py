# biggest value among three numbers

n1 = 10
n2 = 20
n3 = 15
if n1 > n2:
    if n1 > n3:
        print(f'{n1} is big')
    else:
        print(f'{n3} is big')
else:
    if n2 > n3:
        print(f'{n2} is big')
    else:
        print(f'{n3} is big')
        
