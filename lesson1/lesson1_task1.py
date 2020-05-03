# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

secret_number = 23
secret_number_2 = 382

print(f"my secret number {secret_number}")
print('save in secret my secret number 2: {}'.format(secret_number_2))
print('save in secret my secret number 2: %d' % secret_number)

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
print(f"Здравствуйте {name}")
print(f"Вам сейчас {age} и через 10 лет, по моим скромным подсчетам вам будет {age + 10}")


