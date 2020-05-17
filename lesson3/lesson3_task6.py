"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""


def int_func(user_string_list):
    tmp_str = " "
    return tmp_str.join(user_string_list).title()


def main():
    pass

    user_string_list = input("Введите слова через пробел: ").split(" ")

    res = int_func(user_string_list)
    print(res)

    print("Программа завершена")


if __name__ == "__main__":
    main()
