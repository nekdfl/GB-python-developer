# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

import random
from .bill import Bill


class BillGenerator:
    pass

    _released_bill = 0

    def __init__(self, min_num=1, max_num=90, str_in_bill=3, el_in_str=9, num_in_str=6):
        self._min_num = min_num
        self._max_num = max_num
        self._str_in_bill = str_in_bill
        self._el_in_str = el_in_str
        self._num_in_str = num_in_str
        self._src_list = list(range(self._min_num, self._max_num + 1))

    def _get_str(self):

        res = []
        spc_cnt = self._el_in_str - self._num_in_str
        num_in_str = 0
        for idx in range(self._el_in_str):
            if num_in_str == self._num_in_str:
                res.append("".rjust(4))
                spc_cnt -= 1
            elif random.randrange(1, 11) % 2 == 0 and spc_cnt > 0:
                res.append("".rjust(4))
                spc_cnt -= 1
            else:
                res.append(f" {self._src_list.pop(idx)} ".rjust(4))
                num_in_str += 1

        return res

    def generate_bill(self):
        bill_data = []
        self._src_list = list(range(self._min_num, self._max_num + 1))
        random.shuffle(self._src_list)
        for _ in range(self._str_in_bill):
            bill_data.append(self._get_str())
        self._released_bill += 1
        bill = Bill(self._released_bill, bill_data)
        return bill

    @property
    def released_count(self):
        return self._released_bill
