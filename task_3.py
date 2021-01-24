# Для этой задачи можно использовать встроенную hash функцию
user_str = input("Введите строку: ")
result_lists = []
for i in range(0, len(user_str) + 1):
    for n in range(i + 1, len(user_str) + 1):  # 2 цикла задают переборку всех вариантов, т.е [0:1], [0:2], [1:1] и тд
        if int(result_lists.count(hash(user_str[i:n]))) == 0:  # если такого хеша нет, добавляем его в список.
            result_lists.append(hash(user_str[i:n]))
        # print(hash(user_str[i:n]))
print(f'Колличество различных подстрок равно {len(result_lists)}')
