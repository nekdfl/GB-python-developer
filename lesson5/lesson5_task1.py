"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

"""


def main():

    run_program = True
    with open("task1_data.txt", "w") as f:
        while run_program:
            user_str = input("введите строку для записи: ")
            if user_str == "":
                run_program = False
            else:
                f.write(user_str + "\n")



    print("Программа завершена")


if __name__ == "__main__":
    main()
