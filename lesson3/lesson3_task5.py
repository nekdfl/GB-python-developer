# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.


def get_user_data_list():
    user_data = input("Введите числа через пробел: ")
    return user_data.split(" ")


def __get_value_from_item(item):
    got_point = False
    tmp_str = ""
    got_breakchar = False
    res = ""
    for ch in list(item):
        if ch.isalnum():
            tmp_str += ch
        elif ch == ".":
            got_point = True
            tmp_str += ch
        else:
            got_breakchar = True
            break
    if tmp_str == ".":
        got_breakchar = True

    if not got_breakchar:
        if got_point:
            res = float(tmp_str)
        else:
            res = int(tmp_str)

    return got_breakchar, res


def get_summ_user_data_list(user_data_list):
    res_list = []
    got_breakchar = False
    for item in user_data_list:
        if item == "":
            continue

        got_breakchar, res = __get_value_from_item(item)

        if got_breakchar is True:
            break
        else:
            res_list.append(res)

    summa = sum(res_list)
    return summa, got_breakchar


def variant1():
    ascii_num_char_range = range(48, 58)
    got_breakchar = False
    summa = 0

    print("Программа принимает целые и вещественные числа.")
    print("Программа игнорирует пустые значения (дойной пробел)")
    print("Но при вводе любого символа, спецсимвола или точки завершиться")

    while not got_breakchar:
        user_data_list = get_user_data_list()
        res, got_breakchar = get_summ_user_data_list(user_data_list)
        summa += res
        print(f"накопленная сумма: {summa}")


def get_summ_user_data_list_v2(user_data_list):
    res_list = []
    got_breakchar = False
    for item in user_data_list:

        if item.count("!") > 0:
            got_breakchar = True
            break

        if item.count(".") == 1:
            try:
                num = float(item)
                res_list.append(num)
            except ValueError:
                pass
        else:
            try:
                num = int(item)
                res_list.append(num)
            except ValueError:
                pass

    summa = sum(res_list)
    return summa, got_breakchar


def varian2():
    got_breakchar = False
    summa = 0

    print("Программа принимает целые и вещественные числа.")
    print("Программа игнорирует пустые значения (дойной пробел), а также все символы")
    print("Но при вводе символа '!' программа завершиться")

    while not got_breakchar:
        user_data_list = get_user_data_list()
        res, got_breakchar = get_summ_user_data_list_v2(user_data_list)
        summa += res
        print(f"накопленная сумма: {summa}")


def main():
    pass


    # variant1()
    varian2()
    print("Программа завершена")


if __name__ == "__main__":
    main()

