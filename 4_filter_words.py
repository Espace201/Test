def f (x):
	return x == x[::-1]

a = ('яблоко', 'заказ', 'окно', 'шалаш','дверь', 'кот', 'дед')
b = tuple(filter(f, a))
print(b)
