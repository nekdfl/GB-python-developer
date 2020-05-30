"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.

"""


class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print(f"{self._title}: stationery draw method ")


class Pencil(Stationery):

    def draw(self):
        print(f"{self._title}: pencil draw method")


class Handle(Pencil):

    def draw(self):
        print(f"{self._title}: handle draw method")


def main():
    stationary = Stationery("Перо")
    pencil = Pencil("карандаш 3м")
    handle = Handle("Маркер")
    stationary.draw()
    pencil.draw()
    handle.draw()
    print("Программа завершена")


if __name__ == "__main__":
    main()
