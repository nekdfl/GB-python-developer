# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = ["2", "1", "4", "3", "6", "5", "7"]

user_data = input("Введите значения через пробел: ")
my_list = user_data.rstrip(" ").split(" ")  # предпочитаю явно указать пробел как разделитель
print(f"входной список \t\t{my_list}")

# idx = 0
# while idx < len(my_list):
#     if (idx + 1) % 2 == 0:
#         cur = my_list[idx]
#         prev = my_list[idx - 1]
#         my_list[idx] = prev
#         my_list[idx - 1] = cur
#
#     idx += 1

# работа над ошибками
# наверно можно через генератор сразу список сделать индексов
for el_num, item in enumerate(my_list):
    # print(f"{bool(el_num % 2 == 0)}; elnum:{el_num} ; item:{item}")
    if el_num % 2 != 0:
        tmp = my_list.pop(el_num)
        my_list.insert(el_num - 1, tmp)


print(f"выходной список \t{my_list}")
