# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import signal
from lotogame import LotoGame


# MainApp = singleton с отложенным созданием экземпляра


class MainApp:
    __instance = None

    def init(self, playername, bill_count):
        self.__game = LotoGame(playername, bill_count)

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = MainApp()
        return cls.__instance

    def do_game(self):
        while not self.__game.do_we_have_winner():
            self.__game.make_step()

    def loop(self):
        finish_game = False
        while not finish_game:
            self.do_game()

            repeat_game = LotoGame.ask_repeat("Съиграем еще раз?")
            if repeat_game == False:
                finish_game = True


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
    playername = LotoGame.ask_playername()
    bill_count = LotoGame.ask_bill_count()
    mainapp = MainApp()
    mainapp.get_instance()
    mainapp.init(playername, bill_count)
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    print('Running. Press CTRL-C to exit.')
    mainapp.loop()
    print("Программа завершена")


if __name__ == "__main__":
    main()
