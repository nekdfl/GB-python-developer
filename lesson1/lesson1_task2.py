# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input("Введите время в секундах: "))

# test_h = 0
# test_m = 45
# test_sec = 12
# time_in_seconds = 3600 * test_h + 60 * test_m + test_sec

hours = int(time_in_seconds // 3600)
hours_in_seconds = hours * 3600
minutes = int((time_in_seconds - hours_in_seconds) // 60)
minutes_in_seconds = minutes * 60
seconds = int(time_in_seconds - hours_in_seconds - minutes_in_seconds)

# ugly version
# print(f"Время %.2d:%.2d:%.2d" % (hours, minutes, seconds))
# less ugly version
# print("Время {:>02}:{:>02}:{:>02}".format(hours, minutes, seconds))

# beautiful version
print(f"Время {hours:>02d}:{minutes:>02d}:{seconds:>02d}")
