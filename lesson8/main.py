# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import signal
from lotogame import LotoGame


# MainApp = singleton с отложенным созданием экземпляра


class MainApp:
    __instance = None

    def init(self, playername):
        self.__playername = playername


    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = MainApp()
        return cls.__instance

    def loop(self):
        finish_game = False
        player_fault = False
        self.__game = LotoGame(self.__playername)

        while not finish_game:

            while not self.__game.do_we_have_winner():
                player_fault = self.__game.make_step()
                if player_fault:
                    break

            answer = LotoGame.ask_yesno("Съиграем еще раз?")
            if answer == False:
                finish_game = True
            else:
                player_fault = False
                self.__game = LotoGame(self.__playername)


def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


def init():
    pass
    # init logger
    # init config
    # update logger config


def main():
    LotoGame.print_logo()
    LotoGame.print_rules()
    playername = LotoGame.ask_player_name()
    # bill_count = LotoGame.ask_interger_num()
    mainapp = MainApp()
    mainapp.get_instance()
    mainapp.init(playername)
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    print('Running. Press CTRL-C to exit.')
    mainapp.loop()
    print("Программа завершена")


if __name__ == "__main__":
    main()
