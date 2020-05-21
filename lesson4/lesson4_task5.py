"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""

from functools import reduce


def mugnification(prev_el, el):
    return int(prev_el) * int(el)


def main():
    odd_list = [el for el in range(100, 1001) if el % 2 == 0]
 

    print(reduce(mugnification, odd_list))
    print("Программа завершена")


if __name__ == "__main__":
    main()
