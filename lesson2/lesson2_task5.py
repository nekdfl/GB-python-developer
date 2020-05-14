# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_list = [0, 0, 1, 8]
print(f"У нас есть рейтинг. {my_list}")

# проверка ввода
try:
    number = int(input("Введите целое число от 0 до 9: "))
    if number > 9 or number < 0:
        raise RuntimeError(f"Ваше число {number}, вне диапазона 0-9!")
    if type(number) is not int:
        raise RuntimeError(f"Ваше число {number}, не целого типа!")

except RuntimeError as e:
    print(f"{e}")
except ValueError:
    print("Ваше значение не удовлетворяет условию целое число от 0 до 9")

# если числа нет в списке, ищем место для в списке
if my_list.count(number) == 0:
    pos_range = range(0 + 1, len(my_list) + 1)  # +1 для смещения, так как начали с 1 а не с 0

    for num, val in zip(pos_range, my_list):
        # if val > number:
        #     my_list.insert(num, number)
        #     print(f"Вставка в позицию {len(num)}")
        #     break

        if my_list.count(number) == 0:
            my_list.insert(len(my_list), number)
            print(f"Вставка в позицию {len(my_list)}")
else:
    idx = my_list.index(number)
    my_list.insert(idx, number)
    print(f"Вставка в позицию {idx}")

print(f"У нас есть рейтинг. {my_list}")
