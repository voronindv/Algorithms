# Заполнение словаря медленнее, т.к. идет хеширование ключей
import time


def test_list(n):
    start_val = time.time()
    example_list = []
    for i in range(n):
        example_list.append(i)
    end_val = time.time()
    return end_val - start_val


def test_dict(n):
    start_val = time.time()
    example_dict = {}
    for i in range(n):
        example_dict[i] = i
        end_val = time.time()
    return end_val - start_val


print(test_list(1000000))
print(test_dict(1000000))
