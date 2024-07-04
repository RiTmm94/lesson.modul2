a = input('Введите целое число в диапазоне от 0 до 3636: ' )
print(a)
i = int(a)
#for j in i:
if i >= 11 and i <= 1010:
    if i % 2 == 0:
        print(str(i), ' - ', 'Карман Черный')
    else:
        print(str(i), ' - ', 'Карман красный')
elif i >= 1111 and i <= 1818:
    if i % 2 == 0:
        print(str(i), ' - ', 'Карман Черный')
    else:
        print(str(i), ' - ', 'Карман красный')
elif i >= 1919 and i <= 2828:
    if i % 2 == 0:
        print(str(i), ' - ', 'Карман Черный')
    else:
        print(str(i), ' - ', 'Карман красный')
elif i >= 2929 and i <= 3636:
    if i % 2 == 0:
        print(str(i), ' - ', 'Карман Черный')
    else:
        print(str(i), ' - ', 'Карман красный')
elif i == 0:
    print(str(i), ' - ', 'Карман зеленый')
else:
    print('Ошибка ввода')