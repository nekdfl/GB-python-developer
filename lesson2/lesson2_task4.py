#  Пользователь вводит строку из нескольких слов, разделённых пробелами.
#  Вывести каждое слово с новой строки.
#  Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input("Введите несколько слов через пробел: ")
data_list = user_string.split(" ")

for data in data_list:
    print(f"{data[:10]}")