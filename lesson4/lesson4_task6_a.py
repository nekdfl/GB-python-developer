"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

"""
from itertools import count


def get_list_count(start, stop):
    res_list = []

    for el in count(start):
        if el > stop:
            break
        else:
            res_list.append(el)

    return res_list


def main():
    my_list = get_list_count(3, 10)
    print(my_list)

    print("Программа завершена")


if __name__ == "__main__":
    main()
