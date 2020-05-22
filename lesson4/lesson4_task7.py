"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""

from functools import reduce
from itertools import count


def get_list_count(start, stop):
    res_list = []

    for el in count(start):
        if el > stop:
            break
        else:
            res_list.append(el)

    return res_list


def mugnification(prev_el, el):
    return int(prev_el) * int(el)


def fact(num):
    fact_list = get_list_count(1, num)
    res = reduce(mugnification, fact_list)
    yield res


def main():
    calc_fact_list = [3, 4, 6, 7]
    for cfl in calc_fact_list:
        for el in fact(cfl):
            print(f"Факториал {cfl} = {el}")

    print("Программа завершена")


if __name__ == "__main__":
    main()
