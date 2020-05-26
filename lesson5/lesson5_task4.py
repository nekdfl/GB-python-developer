"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""


def readfile(filepath):
    res = ""

    with open(filepath, 'r') as f:
        res = f.read()

    return res


def make_dict(task2_data, delimiter=" - "):
    # print(task2_data)
    res_dict = {}
    for lnum, line in enumerate(task2_data.split("\n")):
        lnum += 1  # номер строки начинается с 0
        if line != "":
            try:
                strelemcnt = len(line.split(delimiter))
                if strelemcnt == 2:
                    # print(f"Обработка строки {lnum} ok")
                    word, nn = line.split(delimiter)
                    res_dict[nn] = word

                else:
                    raise RuntimeError(f"Ошибка ввода данных. Неверное количество аргументов в строке {lnum}.")
            except ValueError as e:
                raise ValueError(f"Неверный формат числа в строке {lnum}. Ошибка {e}")

    return res_dict


def translate(en_dict, ru_dict):
    pass
    resdict = {}
    for key in en_dict.keys():
        resdict[key] = ru_dict[key]
    return resdict


def write_dict(filepath, dict, delimeter):
    pass
    lines = []
    for key in dict.keys():
        line = dict[key] + delimeter + key
        lines.append(line)

    with open(filepath, 'w+') as f:
        f.writelines("\n".join(lines))
        f.seek(0)

        print(f"содержимое выходного файла {filepath}\n{f.read()}")


def full_variant():
    infile_name = "task4_data_in.txt"
    outfile_name = "task4_data_out.txt"
    ru_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
    try:
        task2_data = readfile(infile_name)
    except IOError as e:
        print(f"Ошибка работы с файлом: {e}")

    try:
        file_data_dict = make_dict(task2_data)
    except ValueError as e:
        print(f"{e}")
        exit(1)
    except RuntimeError as e:
        print(f"{e}")
        exit(2)

    try:
        resdict = translate(file_data_dict, ru_dict)
        # print(resdict)
    except KeyError as e:
        print(f"В словаре переводчика нет значения для {e}")
        exit(3)

    write_dict(outfile_name, resdict, " - ")
    print("Программа завершена")


def short_variant():
    infile_name = "task4_data_in.txt"
    outfile_name = "task4_data_out.txt"
    ru_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
    en_dict = {'1': 'one', '2': 'Two', '3': 'Three', '4': 'Four'}
    delimeter = " - "
    res_lines = []

    with open(infile_name, "r") as ifile:
        for line in ifile:
            for kword in en_dict.keys():
                if line.count(kword):
                    res_lines.append(ru_dict[kword] + delimeter + kword)

    with open(outfile_name, "w+") as ofile:
        ofile.writelines("\n".join(res_lines))
        ofile.seek(0)
        print(f"содержимое выходного файла {outfile_name}\n{ofile.read()}")


if __name__ == "__main__":
    # main()
    short_variant()
