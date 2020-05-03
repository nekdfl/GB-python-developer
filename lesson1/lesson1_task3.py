# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# variant1

number = input("Введите число: ")

# n = int(number)
# nn = int(number + number)
# nnn = int(number + number + number)
# result = n + nn + nnn
# print(f"Результат: {result}")
#
# # variant 2
# n = int(number)
# nn = int(number * 2)
# nnn = int(number * 3)
# result_2 = n + nn + nnn
# print(f"Результат: {result_2}")

# variant 3
num = int(number)
x = int(num * 1)
xx = int(num * 11)
xxx = int(num * 111)
result_3 = x + xx + xxx
print(f"Результат2: {result_3}")
