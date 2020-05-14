# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


def readValidUserInput():
    try:
        number = int(input("Введите целое число от 0 до 9: "))
        if number > 9 or number < 0:
            raise RuntimeError(f"Ваше число {number}, вне диапазона 0-9!")
        if type(number) is not int:
            raise RuntimeError(f"Ваше число {number}, не целого типа!")
    except RuntimeError as e:
        print(f"{e}")
        exit(1)
    except ValueError:
        print("Ваше значение не удовлетворяет условию целое число от 0 до 9")
        exit(1)

    return number


def print_rating(my_rating):
    print(f"У нас есть рейтинг. {my_rating}")


def insert_unique_value(value, my_rating):
    ins_idx = -1
    for idx, item in enumerate(my_rating):
        # print(idx)
        if item > value:
            if idx == 0:
                ins_idx = idx
                break
            elif idx > 0:
                ins_idx = idx
                break

    if ins_idx == -1:
        print(f"Число {value} больше всех значений в списке. Добавляем в конец списка, значение {value}")
        my_rating.append(value)
    else:
        my_rating.insert(ins_idx, value)
        print(f"Вставка в {ins_idx}, значения {value}")

    print_rating(my_rating)


def insert_exist_value(value, my_rating):
    pass
    ins_idx = -1
    for idx, item in enumerate(my_rating):
        if item == value and ins_idx == -1:
            ins_idx = idx

        if item > value and ins_idx != -1:
            break

    my_rating.insert(ins_idx, value)
    print(f"Вставка в {ins_idx}, значения {value}")

    print_rating(my_rating)


def do_tests(my_rating):
    test_input_list = [0, 1, 3, 9, 5]
    for value in test_input_list:
        # print(f"{value}")
        if my_rating.count(value) == 0:
            pass
            print(f"Алгоритм поска места для нового элемента: '{value}'")
            insert_unique_value(value, my_rating)
        else:
            print("Алгоритм поска местя для элемента в списке")
            insert_exist_value(value, my_rating)


def do_update_rating(value, my_rating):
    if my_rating.count(value) == 0:
        print(f"Алгоритм поска места для нового элемента: '{value}'")
        insert_unique_value(value, my_rating)
    else:
        print("Алгоритм поска местя для элемента в списке")
        insert_exist_value(value, my_rating)


def main():
    pass
    my_rating = [1, 1, 3, 3, 8]

    number = readValidUserInput()
    print_rating(my_rating)
    # do_tests(my_rating)
    do_update_rating(number, my_rating)


if __name__ == "__main__":
    main()
