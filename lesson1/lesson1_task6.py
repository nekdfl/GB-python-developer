# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров. Программа должна принимать значения
# параметров a и b и  выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# удаляет лишние нули.
def pretty_distance(number):
    distance = f"{number:.2f}".rstrip("0").rstrip("0").rstrip(".")
    return distance


distance_first_day = int(input("Введите сколько спортсмен пробежал в первый день км: "))
distance_target = int(input("Введите цель тренировок км: "))

# distance_first_day = 2
# distance_target = 3

current_distance = distance_first_day
day = 1

while current_distance < distance_target:
    print(f"{day}-й день: {pretty_distance(current_distance)}")

    day += 1
    current_distance += current_distance / 100 * 10

print(f"{day}-й день: {pretty_distance(current_distance)}")
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {int(distance_target)} км.")
