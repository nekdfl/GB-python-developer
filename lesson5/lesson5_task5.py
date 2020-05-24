"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


"""

from random import randrange


def get_random_strlist(start, stop, size):
    """

    :param start: value for start range
    :param stop: value for end range
    :param size: target count of elements in the new list
    :return: list
    """
    new_list = []
    for _ in range(0, size):
        new_list.append(str(randrange(start, stop+1)))

    return new_list


def genfile(filepath, start, end, count):
    """
    генерирует файл со случайными числами
    :param filepath:
    :param start: начиная с числа
    :param end: заканчивая числом
    :param count: количество чисел
    :return:
    """
    res_lsit = get_random_strlist(start, end, count)
    print(res_lsit)

    with open(filepath, 'w+') as ofile:
        ofile.write(" ".join(res_lsit))


def readfile(filepath):
    res = ""
    with open(filepath, 'r') as f:
        res = f.read()

    return res


def main():
    outfile_name = "task5_data_out.txt"

    genfile(outfile_name, 0, 1, 10)
    res_list = readfile(outfile_name).split(" ")

    sum_of_list = sum(map(int, res_list))
    print(f"Сумма чисел {res_list} = {sum_of_list}")

    print("Программа завершена")


if __name__ == "__main__":
    main()
