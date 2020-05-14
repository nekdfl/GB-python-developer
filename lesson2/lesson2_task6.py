# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


def print_list(datalist):
    print("[")
    for item in datalist:
        print(item)
    print("]")


def infill_storage_data():
    storage_data_list = []
    goods_list = input("Введите через пробел список товаров: ").split(" ")
    for good_name in goods_list:
        good_price = int(input(f"Введите цену для {good_name}: "))
        good_count = int(input(f"Введите количество для {good_name}: "))
        mesure_unit = input(f"Введите единицу измерений для {good_name} [шт]: ") or "шт"
        storage_data_list.append({"название": good_name,
                                  "цена": good_price,
                                  "колличество": good_count,
                                  "ед": mesure_unit})
    return  storage_data_list


def convert_data_to_tuple_list(storage_data_list):
    tuple_list = []
    for cnt, storage_data_item in enumerate(storage_data_list):
        s = tuple([cnt, storage_data_item])
        tuple_list.append(s)

    return tuple_list


def convert_tuple_to_analytic(tuple_list):
    analytic_goods_list = []
    key_list = tuple_list[0][1].keys()

    for key in key_list:
        char_list = []
        for item in tuple_list:
            # data_dict = {item[1].get(key),}
            good_charect = item[1].get(key)
            char_list.append(good_charect)
        analytic_goods_list.append({key: char_list})

    return analytic_goods_list


def main():
    storage_data_list = []
    print("Ввод данных для инвенторизации на складе")
    storage_data_list =infill_storage_data()
    print("Превращаем ввод в список кортежей")
    tuple_list = convert_data_to_tuple_list(storage_data_list)
    print("Получился список кортежей")
    print_list(tuple_list)
    print("Собираю аналитику")
    analytic_goods_list = convert_tuple_to_analytic(tuple_list)
    print("Вывожу аналитику")
    print_list(analytic_goods_list)


if __name__ == "__main__":
    main()
