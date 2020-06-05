# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


class Bill:
    pass

    def __init__(self, serial, bill_data):
        self._bill_data = bill_data
        self._serial = serial
        self.__striked_cnt = 0

    @property
    def bill_data(self):
        return self._bill_data

    @property
    def serial(self):
        return self._serial

    def __str__(self):
        res = f"Лотерейный билет №{self._serial}\n"
        for st in self._bill_data:
            res += "-" * (5 * 9 + 1) + "\n"
            res += "|"
            for el in st:
                res += f"{el}|"
            res += "\n"
        res += "-" * (5 * 9 + 1) + "\n"
        return res

    def have_num(self, num):
        for st in self._bill_data:
            for el in st:
                if el == f" {num} ".rjust(4):
                    return True

        return False

    def strike(self, num):
        for st in self._bill_data:
            for idx, el in enumerate(st):
                if el == f" {num} ".rjust(4):
                    el = el.replace(" ", "-")
                    self.__striked_cnt += 1
                    st[idx] = el

    @property
    def striked_cnt(self):
        return self.__striked_cnt
