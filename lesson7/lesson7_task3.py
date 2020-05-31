"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству
ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.

"""


class Nucleos:

    def __init__(self, data):
        self._cells_count = data

    @property
    def cells_count(self):
        return self._cells_count

    def __add__(self, other):
        nucleo = Nucleos(self._cells_count + other.cells_count)
        return nucleo

    def __sub__(self, other):
        cell_cnt = self._cells_count - other.cells_count
        if cell_cnt < 0:
            raise RuntimeError("Результат разности клеток - отрицательный")

        nucleo = Nucleos(cell_cnt)
        return nucleo

    def __mul__(self, other):
        nucleo = Nucleos(self._cells_count * other.cells_count)
        return nucleo

    def __truediv__(self, other):
        nucleo = Nucleos(self._cells_count // other.cells_count)
        return nucleo

    def __str__(self):
        return str(self._cells_count)

    @staticmethod
    def make_order(nucleos, cnt):
        pass
        nc_cnt = int(str(nucleos.cells_count))
        full_cycle = nc_cnt // cnt
        out_of_cycle = nc_cnt % cnt

        for i in range(full_cycle):
            print("*" * cnt)

        if out_of_cycle > 0:
            print("*" * out_of_cycle)


def main():
    a = Nucleos(12)
    b = Nucleos(5)

    c = Nucleos(a + b)
    d = Nucleos(a - b)
    e = Nucleos(a * b)
    f = Nucleos(a / b)
    print(f"+\t| -\t| *\t| /\t|")
    print(f"{c}\t| {d}\t| {e}\t| {f}")

    Nucleos.make_order(c, 6)

    print("Программа завершена")


if __name__ == "__main__":
    main()
