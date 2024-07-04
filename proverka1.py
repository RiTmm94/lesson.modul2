import random

a = input('Введите первое целое число: ' )
print(a)
b = input('Введите второе целое число: ' )
print(b)
c = ['+', '-', '*', '/']
c1 = random.choice(c)
if c1 == '+':
    print(str(a), '+', str(b))
    sum = int(a) + int(b)
    #print(sum)
elif c1 == '-':
    print(str(a), '-', str(b))
    sum = int(a) - int(b)
    #print(sum)
elif c1 == '*':
    print(str(a), '*', str(b))
    sum = int(a) * int(b)
    #print(sum)
elif c1 == '/':
    print(str(a), '/', str(b))
    sum = int(a) / int(b)
print(sum)