# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

from .player import Player


class LotoGame:
    pass

    def __init__(self, playername, bill_count):
        pass

    @staticmethod
    def print_rules():
        print("""Вы вводите ваше имя и количество билетов учавствующих в игре
    Как только есть билет в котором совпали все цифры в строке или все цифры в строка, игра заканчивается и 
    объявляется победитель.
    Для выхода из игры нужно нажать CTRL + c""")

    @staticmethod
    def print_logo():
        print("                 Р У С С К О Е                \n"
              "    * * * *   * * * * *  * * * * *   * * * * *\n"
              "   *      *   *       *      *       *       *\n"
              "   *      *   *       *      *       *       *\n"
              "   *      *   *       *      *       *       *\n"
              "   *      *   *       *      *       *       *\n"
              " ***      *   * * * * *      *       * * * * *\n")

    @staticmethod
    def ask_repeat(text="повторить ввод?"):
        answer = input(f"{text} y/[n]: ")
        if answer == "y":
            return True
        return False

    @staticmethod
    def ask_bill_count():
        try:
            bill_count = int(input("Введите число генерируемых билетов лото: "))
        except ValueError as e:
            print("Ошибка! Количество билетов, должно быть целым числом.")
            if LotoGame.ask_repeat():
                LotoGame.ask_bill_count()
        else:
            bill_count = 0

        return bill_count

    @staticmethod
    def ask_playername():
        player_name = input("Введите имя игрока: ")
        return player_name

    def prepare_game(self):
        pass

    def make_step(self):
        pass

    def do_we_have_winner(self):
        pass
        return True


def main():
    pass
    lotogame = LotoGame("nek", 3)
    lotogame.prepare_game()
    while not lotogame.do_we_have_winner():
        lotogame.make_step()

    print("Программа завершена")


if __name__ == "__main__":
    main()
