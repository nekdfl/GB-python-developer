"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.


"""
import time


class Traffic_light():

    def __init__(self):
        pass
        self._r_sleep = 7
        self._y_sleep = 2
        self._g_sleep = 5
        self.__color = "RED"

    def _down(self):
        self.__color = "RED"
        print(f"Currents state {self.__color}")
        time.sleep(self._r_sleep)
        self.__color = "Yellow"
        print(f"Currents state {self.__color}")
        time.sleep(self._y_sleep)
        self.__color = "Green"
        print(f"Currents state {self.__color}")
        time.sleep(self._g_sleep)

    def _up(self):
        self.__color = "Yellow"
        print(f"Currents state {self.__color}")
        time.sleep(self._y_sleep)
        self.__color = "RED"
        print(f"Currents state {self.__color}")

    def running(self):
        pass
        self._down()
        self._up()


def main():
    my_tf = Traffic_light()
    my_tf.running()

    print("Программа завершена")


if __name__ == "__main__":
    main()
