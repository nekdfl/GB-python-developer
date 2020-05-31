"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т


"""


class Road():

    def __init__(self, length, width):
        pass
        self._length = length
        self._width = width

    def calc(self, mass, height):
        kg = self._length * self._width * mass * height
        return kg


def main():
    trassa_e95 = Road(5000, 20)
    mass_need = trassa_e95.calc(25, 5) / 1000

    print(f"Нам нужно {mass_need} тонн")

    print("Программа завершена")


if __name__ == "__main__":
    main()