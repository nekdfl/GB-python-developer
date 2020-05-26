"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

"""


def readfile(filepath):
    pass
    res = ""

    with open(filepath, 'r') as f:
        res = f.read()

    return res


def make_listdict(task2_data):
    # print(task2_data)
    res_list = []
    for lnum, line in enumerate(task2_data.split("\n")):
        lnum += 1  # номер строки начинается с 0
        try:
            if len(line.split(" ")) == 2:
                # print(f"Обработка строки {lnum} ok")
                name, salary = line.split(" ")
                salary = float(salary)
                item = {"name": name, "salary": salary}
                res_list.append(item)

            else:
                raise RuntimeError(f"Ошибка ввода данных. Неверное количество аргументов в строке {lnum}.")
        except ValueError as e:
            raise ValueError(f"Неверный формат числа в строке {lnum}. Ошибка {e}")

    return res_list


def main():
    file_name = "task3_data.txt"
    try:
        task2_data = readfile(file_name)
    except IOError as e:
        print(f"Ошибка работы с файлом: {e}")

    try:
        file_data_listdict = make_listdict(task2_data)
    except ValueError as e:
        pass
        print(f"{e}")
    except RuntimeError as e:
        pass
        print(f"{e}")

    print("Список сотрудников с ЗП меньше 20 000")

    salary_sum = 0.0
    for el in file_data_listdict:
        if el["salary"] < 20000:
            print(f'{el["name"]}')
        salary_sum += el["salary"]

    salary_mid_range = salary_sum / len(file_data_listdict)
    print(f"Средняя ЗП: {salary_mid_range:>.2f}")

    print("Программа завершена")


if __name__ == "__main__":
    main()
