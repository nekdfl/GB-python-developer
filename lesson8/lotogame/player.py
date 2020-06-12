# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

class Player:

    def __init__(self, name, bill):
        self._name = name
        self._bill = bill

    @property
    def name(self):
        return self._name

    @property
    def bill(self):
        return self._bill
