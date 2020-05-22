"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

"""
from itertools import cycle
from random import randrange


def get_random_list(start, stop, size):
    """

    :param start: value for start range
    :param stop: value for end range
    :param size: target count of elements in the new list
    :return: list
    """
    new_list = []
    for _ in range(0, size):
        new_list.append(randrange(start, stop))

    return new_list


def main():
    new_list = get_random_list(1, 100, 3)
    res_list = []
    cnt = 0
    target_element_count = 10
    print(new_list)
    for el in cycle(new_list):
        if cnt > target_element_count:
            break
        else:
            res_list.append(el)
            print(res_list)
        cnt += 1
    print("*" * 40)
    print(f"res list = \n"
          f"{res_list}")
    print("Программа завершена")


if __name__ == "__main__":
    main()
