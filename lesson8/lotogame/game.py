# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

from lotogame.billgenerator import BillGenerator
from lotogame.bill import Bill
from lotogame.lototron import LotoTron
from lotogame.player import Player


class LotoGame:

    def __init__(self, playername):
        pass
        self.__player_name = playername
        self._str_in_bill = 3
        self._num_in_str = 5
        min_num = 1
        max_num = 90
        el_in_str = 9
        bg = BillGenerator(min_num, max_num, self._str_in_bill, el_in_str, self._num_in_str)
        player_bill = bg.generate_bill()
        self._player = Player(self.__player_name, player_bill)
        computer_bill = bg.generate_bill()
        self._computer = Player("computer", computer_bill)
        self.__lototron = LotoTron(min_num, max_num)

    @staticmethod
    def print_rules():
        print("""Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

----------------------------------------------
|    |    |    | 43 |    | 60 | 52 | 42 | 68 |
----------------------------------------------
| 14 | 76 | 36 | 46 |    |    | 82 |    |    |
----------------------------------------------
|    |    |    | 44 |    | 17 | 30 | 16 | 79 |
----------------------------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
Если цифра есть на карточке - она зачеркивается и игра продолжается.
Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
Если цифра есть на карточке - игрок проигрывает и игра завершается.
Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Для выхода из игры нужно нажать CTRL + c""")

    @staticmethod
    def print_logo():
        print("                    ЭКСПРЕСС                  \n"
              "    * * * *   * * * * *  * * * * *   * * * * *\n"
              "   *      *   *       *      *       *       *\n"
              "   *      *   *       *      *       *       *\n"
              "   *      *   *       *      *       *       *\n"
              "   *      *   *       *      *       *       *\n"
              " ***      *   * * * * *      *       * * * * *\n")

    @staticmethod
    def ask_yesno(text="повторить ввод?"):
        answer = input(f"{text} y/[n]: ")
        if answer == "y":
            return True
        return False

    @staticmethod
    def ask_interger_num(text="Введите число?"):
        try:
            bill_count = int(input(f"{text}: "))
        except ValueError as e:
            print("Ошибка! Число допустимы только целые числа.")
            if LotoGame.ask_yesno():
                LotoGame.ask_interger_num()
        else:
            bill_count = 0

        return bill_count

    @staticmethod
    def ask_player_name():
        player_name = input("Введите имя игрока: ")
        return player_name



    def make_step(self):
        print(f"Билет игрока {self._computer.name}")
        print(self._computer.bill)

        print(f"Билет игрока {self._player.name}")
        print(self._player.bill)

        keg = self.__lototron.get_next_keg()
        self._computer.bill.strike(keg)

        answer = self.ask_yesno(f"у вас есть число {keg} в билете?")
        player_have_keg = self._player.bill.have_num(keg)
        game_end = False
        if answer != player_have_keg:
            game_end = True
            if self._player.bill.have_num(keg):
                print(f"Игрок пропустил число {keg} в своем билете. Вы проиграли.")
            else:
                print(f"В вышем билете нет числа {keg}. Вы проиграли.")
        elif player_have_keg:
            self._player.bill.strike(keg)
            print(self._player.bill)
        return game_end

    def do_we_have_winner(self):
        """
        :return: True if have full striked Bill
        """
        max_num_in_bill = self._str_in_bill * self._num_in_str
        have_winner = False
        if self._player.bill.striked_cnt == max_num_in_bill:
            print(f"Игрок {self._player.name} выйграл")
            have_winner = True

        if self._computer.bill.striked_cnt == max_num_in_bill:
            print(f"Игрок {self._player.name} выйграл")
            have_winner = True

        return have_winner


def main():
    pass
    # lotogame = LotoGame("nek")
        # while not lotogame.do_we_have_winner():
    #     lotogame.make_step()

    print("Программа завершена")


if __name__ == "__main__":
    main()
