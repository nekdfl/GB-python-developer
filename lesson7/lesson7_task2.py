"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    pass

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.__v = v

    @property
    def material(self):
        res = self.__v / 6.5 + 0.5
        return res


class Costume:
    pass

    def __init__(self, h):
        self.__h = h

    @property
    def material(self):
        res = 2 * self.__h + 0.3
        return res


def main():
    little_coat = Coat(6)
    big_coat = Coat(10)
    little_suit = Costume(4)
    big_suit = Costume(12)

    print("Планируемый расход материала М")
    print(f"маленький плащ {little_coat.material}")
    print(f"большой плащ {big_coat.material}")
    print(f"маленький косюм {little_suit.material}")
    print(f"большой костюм {big_suit.material}")

    print("Программа завершена")


if __name__ == "__main__":
    main()
