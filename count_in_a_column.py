user_input = input("Введите строку: ").lower()
set1 = set(user_input)
max_len = 1
for symbol in set1:
    if symbol.isalpha() and max_len < user_input.count(symbol):
        max_len = user_input(symbol)
for symbol in set1:
    if symbol.isalpha():
        print(f"| {symbol} | {user_input.count(symbol):<{len(str(max_len))}} |")