a = input('Введите число: ')
b = a.count('.')
if a.isdigit() or b == 1 or a[0] == '-' and a[1:].isdigit():
    a = float(a)

    if a > 0:
        print('Число положительное')
    elif a < 0:
        print('Число отрицательное')
    elif a == 0:      print('Ноль')

else:
    print('Введите число')

