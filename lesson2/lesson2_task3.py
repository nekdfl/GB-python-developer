#  Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#  Напишите решения через list и через dict.

winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]

season_dict = {1: "зима",
               12: "зима",
               2: "зима",
               3: "весна",
               4: "весна",
               5: "весна",
               6: "лето",
               7: "лето",
               8: "лето",
               9: "осень",
               10: "осень",
               11: "осень"}
try:
    month = int(input("Введите номер месяца(1-12): "))
except ValueError:
    print("Неправильное число")
    exit(1)

if month < 1 or month > 12:
    print("Номер месяца должен быть от 1 до 12")
    exit(2)

print("Ищу в словаре...")
print(season_dict.get(month)) if season_dict.get(month) else print("Wrong number of month")

print("Ищу в списке...")
if winter_list.count(month):
    print("зима")
elif spring_list.count(month):
    print("весна")
elif spring_list.count(month):
    print("лето")
elif autumn_list.count(month):
    print("осень")
else:
    print("Wrong number of month")

