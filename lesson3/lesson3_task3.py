"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(num1, num2, num3):
    pass
    varlist = [num1, num2, num3]

    sumarg1 = max(varlist)
    varlist.pop(varlist.index(sumarg1))
    sumarg2 = max(varlist)
    res = sumarg1 + sumarg2

    return res


def main():
    pass
    res = my_func(1, 2, 3)
    print(res)


if __name__ == "__main__":
    main()
