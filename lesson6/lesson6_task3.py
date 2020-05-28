"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        pass
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self._surname + " " + self._name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


def main():
    chief = Position("Сергей", "Васильев", "Начальник", 20000, 5000)
    cleaner = Position("Виталий", "Борисенко", "Дворник", 10000, 1000)

    print(f"{chief.get_full_name()} получает {chief.get_total_income():.2f}")
    print(f"{cleaner.get_full_name()} получает {cleaner.get_total_income():.2f}")


    print("Программа завершена")


if __name__ == "__main__":
    main()
