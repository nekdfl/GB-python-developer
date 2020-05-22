"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv
import os

from sys import argv


def show_help():
    selffilename = os.path.basename(argv[0])
    print("Программа расчета заработной платы сотрудника.\n",
          "расчет ведется по формуле 'выработка в часах*ставка в час + премия'\n",
          "Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.\n",
          f"{selffilename} выработка_в_часах ставка_в_час премия\n",
          f"пример {selffilename} 50 8.5 200\n")


def parse_args():
    print(argv)
    if len(argv) != 4:
        show_help()
        raise RuntimeError("wrong arguments count.")

    hours = float(argv[1])
    rate_per_hour = float(argv[2])
    award = float(argv[3])

    return hours, rate_per_hour, award


def do_calc(hours, rate_per_hour, award):
    res = hours * rate_per_hour + award
    return res


def main():
    try:
        hours, rate_per_hour, award = parse_args()
    except ValueError:
        print("Неверный тип аргумента")
        show_help()
        exit(1)
    except RuntimeError as e:
        print(f"error message: {e[0]}")
        show_help()
        exit(1)

    res = do_calc(hours, rate_per_hour, award)

    print(f"Зарплата {res}")
    print("Программа завершена")


if __name__ == "__main__":
    main()
