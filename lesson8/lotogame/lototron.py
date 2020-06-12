# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import random


class LotoTron:
    pass

    def __init__(self, min_num=1, max_num=90):
        self._min_num = min_num
        self._max_num = max_num
        self._src_list = list(range(self._min_num, self._max_num + 1))
        random.shuffle(self._src_list)

    def get_next_keg(self):
        keg = self._src_list.pop()
        return keg
