import random

LST_LEN = 10

num_lst = [random.randint(0, 11) for _ in range(LST_LEN)]
even_num = []

for i in range(LST_LEN):
    if num_lst[i] % 2 == 0:
        even_num.append(i + 1)

print(f'Базовый массив\n{num_lst}')
print(f'Массив идексов четных чисел\n{even_num}')
