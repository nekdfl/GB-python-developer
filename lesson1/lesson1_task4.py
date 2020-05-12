# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


multi_number = input("введите число: ")
i = 0
res = -1
while i < len(multi_number):
    num = int(multi_number[i])
    if num > res:
        res = num
    i += 1

if res > 0:
    print(f"Самая большая цифра {res}")
else:
    print(f"число {multi_number} не соотвствует условиям. Число должно быть целым и больше 0")
