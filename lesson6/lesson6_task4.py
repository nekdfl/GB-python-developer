"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self._name = name
        self._speed = speed
        self._color = color
        self._is_police = is_police

    def go(self):
        print("go to... point")

    def go(self):
        print("stop")

    def turn(self, direction):
        print(f"Turn to {direction}")

    def show_speed(self):
        print(f"{self._name} = speed: {self._speed}")


class TownCar(Car):
    pass
    __speed_limit = 60

    def show_speed(self):
        if self._speed > self.__speed_limit:
            print(f"{self._name} Get slow! Speed over limit of 60 km/h")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    pass

    __speed_limit = 40

    def show_speed(self):
        if self._speed > self.__speed_limit:
            print(f"{self._name} Get slow! Speed over limit of 60 km/h")
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


def main():
    car = Car("Уаз", 40, "Хакки", True)
    car.show_speed()
    towncar = TownCar("Лада приора", 100, "Баклажан")
    towncar.show_speed()
    sportcar = SportCar("ford mustang", 180, "белый")
    sportcar.show_speed()
    workcar1 = WorkCar("Зил", 60, "бежевый")
    workcar1.show_speed()
    workcar2 = WorkCar("Зил2", 35, "синий")
    workcar2.show_speed()
    print("Программа завершена")


if __name__ == "__main__":
    main()
