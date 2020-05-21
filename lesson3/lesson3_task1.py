"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

import sys


# программа умышленно сделана настойчива на ответ.

def ask_repeat(msg=""):
    res: bool = False
    if len(msg):
        answer = input(f"Хотите повторить {msg} [N]? : ") or "N"
    else:
        answer = input(f"Хотите повторить [N]? : ") or "N"

    if answer.capitalize() == "Y":
        res = True
    else:
        res = False
    return res


def input_argument():
    argument = float(input("Введите делимое: "))
    return argument


def input_devider():
    mydevider = float(input("Введите делитель: "))
    if mydevider == 0.0:
        raise RuntimeError("Значение 0 для делителя недопустимо")
    return mydevider


def do_devide(argument, mydevider):
    result = argument / mydevider
    return result


def show_result(result):
    print(f"результат {result}")


def exit_with_error(msg, errcode):
    print(f"{msg}")
    sys.exit(errcode)


def do_calc():
    try:
        argument = float(input("Введите делимое: "))
    except ValueError:
        msg = "введено недопустимое значение для делимого"
        exit_with_error(msg, 1)

    try:
        devider = input_devider()
    except ValueError:
        msg = "введено недопустимое значение для делителя"
        exit_with_error(msg, 2)
    except RuntimeError as ex:
        msg = ex.args[0]
        exit_with_error(msg, 3)

    res = do_devide(argument, devider)
    show_result(res)


def main():
    do_calc()
    while ask_repeat(""):
        do_calc()


if __name__ == "__main__":
    main()
