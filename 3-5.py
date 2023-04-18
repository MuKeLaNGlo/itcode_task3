# Задание 3
shopping_list: list = ['яблоко', 'банан', 'капуста', 'хлеб', 'творог', 'мясо', 'яйца']
count: int

count = len(shopping_list)

print(f'У тебя {count} продуктов, где {count} — значение переменной count\n')


# Задание 4
print(*shopping_list, sep=', ')
print()

# Задание 5
shopping_list = [item for item in shopping_list if len(item) % 2 == 0]
print(*shopping_list, sep=', ')