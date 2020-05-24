"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика:   100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""


# вместо регулярок
def val_to_valid_int(val):
    filtered_list = [el for el in val if el.isdigit()]
    res_str = ""
    for elem in filtered_list:
        res_str += elem

    num = int(res_str)
    return num


def readfile(filepath):
    pass
    res_dict = {}
    with open(filepath) as f:
        for line in f:
            key, value_part = line.split(":")
            val_list = value_part.split(" ")
            dlist = [el for el in val_list if el != "" and el != "-"]
            hoursum = 0
            for data in dlist:
                hoursum += val_to_valid_int(data)
            res_dict[key] = hoursum
    return res_dict


def main():
    infile_name = "task6_data_in.txt"
    result = readfile(infile_name)
    print(result)
    print("Программа завершена")


if __name__ == "__main__":
    main()
