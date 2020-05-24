"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.


"""


def read_file(path):
    res = []
    with open(path, "r") as f:
        res = f.readlines()

    return res


def main():
    file_name = "task2_data.txt"
    task2_data = read_file(file_name)

    line_count = len(task2_data)
    print(f"в файле {file_name} - {line_count} строк")

    for strn, line in enumerate(task2_data):
        strn += 1  # отсчет с 0
        word_count = len(line.split())
        print(f"в строке {strn} - {word_count} слов")

    print("Программа завершена")


if __name__ == "__main__":
    main()
