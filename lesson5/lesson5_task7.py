"""
Создать вручную и заполнить несколькими строками текстовый файл,
 в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


"""

import json


def readfile_firm_list(filepath):
    pass
    firm_list = []
    with open(filepath) as f:
        for line in f:
            striped_line = line.strip("\n")
            if striped_line != "":
                firm_list.append(striped_line.split())

    return firm_list


def savetojson(filepath, data):
    with open(filepath, 'a+') as f:
        json.dump(data, f, indent=3)


def main():
    infile_name = "task7_data_in.txt"
    outfile_name = "task7_data_out.json"
    firm_dict = {}
    avarage_profit_dict = {}
    profit_sum = 0.0

    firmlist = readfile_firm_list(infile_name)
    print("Список компаний с прибылью:")
    for firm in firmlist:
        name = firm[0]
        income = firm[2]
        loss = firm[3]
        profit = float(income) - float(loss)
        if profit > 0:
            print(f"{name} : {profit:.2f}")
            firm_dict[name] = profit
            profit_sum += profit

    avarage_profit = profit_sum / len(firmlist)
    print(f"Средняя прибыль: {avarage_profit:.2f}")
    avarage_profit_dict["average_profit"] = avarage_profit

    res_dictlist = []
    res_dictlist.append(firm_dict)
    res_dictlist.append(avarage_profit_dict)
    print(res_dictlist)

    savetojson(outfile_name, res_dictlist)

    print("Программа завершена")


if __name__ == "__main__":
    main()
