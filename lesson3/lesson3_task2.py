"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""


def get_user_data(msg):
    res = input(f"Введите {msg}: ")
    return res


def show_greeting(name, third_name, birth_date, city, email, phone):
    print(f"Приветствуем пользователя {third_name} {name}, {birth_date} года рождения")
    print(f"{name} живет в {city}")
    print(f"и очень ждет ваших вопросов по {email} и телефону {phone}")


def main():
    pass
    name = get_user_data("имя")
    third_name = get_user_data("фамилию")
    birth_date = get_user_data("год рождения")
    city = get_user_data("город проживания")
    email = get_user_data("email")
    phone = get_user_data("телефон")
    show_greeting(phone=phone, city=city, name=name, third_name=third_name, birth_date=birth_date, email=email)


if __name__ == "__main__":
    main()
