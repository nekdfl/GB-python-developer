# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.


def show_ascii_spec_list(ascii_char_range):
    for ch in ascii_char_range:
        print(f"{chr(ch)} ", end="")
    print("")


def convert_ascii_range_to_list(ascii_range):
    res = []
    for ch in ascii_range:
        res.append(chr(ch))
    return res


def get_user_data_list():
    user_data = input("Введите числа через пробел: ")
    return user_data.split(" ")


def get_summ_user_data_list(user_data_list, num_char_list):
    res_list = []
    got_breakchar = False
    got_point = False
    for item in user_data_list:
        got_point = False
        tmp_str = ""

        if item == "":
            continue

        if got_breakchar is True:
            break

        for ch in list(item):
            if ch in num_char_list:
                tmp_str += ch
            elif ch == ".":
                got_point = True
                tmp_str += ch
            else:
                got_breakchar = True
                break

        if not got_breakchar:
            if got_point:
                res_list.append(float(tmp_str))
            else:
                res_list.append(int(tmp_str))

    summa = sum(res_list)
    return summa, got_breakchar


def main():
    pass
    got_breakchar = False
    summa = 0
    # ascii_spec_char_range = range(33, 48)
    ascii_num_char_range = range(48, 58)
    # show_ascii_spec_list(ascii_spec_char_range)
    # show_ascii_spec_list(ascii_num_char_range)

    num_char_list = convert_ascii_range_to_list(ascii_num_char_range)

    while not got_breakchar:
        user_data_list = get_user_data_list()
        res, got_breakchar = get_summ_user_data_list(user_data_list, num_char_list)
        summa += res
        print(f"накопленная сумма: {summa}")


if __name__ == "__main__":
    main()
