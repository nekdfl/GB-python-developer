"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д..
"""
from itertools import zip_longest


class Matrix:

    def __init__(self, matrix_data):
        self.__matrix_data = matrix_data

    def __add__(self, other):
        # вложенная функция, чтобы не плодить функции.
        # так и не смог сделать из нее lambda
        def add_lists(a, b):
            c = [sum(i) for i in zip_longest(a, b, fillvalue=0)]
            return c

        res_list = []

        longer = self if len(self.__matrix_data) >= len(other.matrix_by_string) else other

        for i in range(len(longer.matrix_by_string)):
            a = self.matrix_by_string[i]
            b = other.matrix_by_string[i]

            res = add_lists(a, b)
            res_list.append(res)

        res_matrix = Matrix(res_list)
        return res_matrix

    map

    @property
    def matrix_by_string(self):
        return self.__matrix_data

    def __str__(self):
        str_res = ""
        for lst in self.__matrix_data:
            for el in lst:
                str_res += f"{el}\t"
            str_res += "\n"
        return str_res


def main():
    test_data1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    test_data2 = [[1, 1], [1, 1], [1, 1]]

    m1 = Matrix(test_data1)
    m2 = Matrix(test_data2)
    m3 = m1 + m2
    print(f"Матрица1 \n{m1}")
    print(f"Матрица2 \n{m2}")
    print(f"Итоговая матрица \n{m3}")
    print("Программа завершена")


if __name__ == "__main__":
    main()
