### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты:
# <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input("Введите продолжительность периода в секундах: "))

sec = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = (duration // (3600 * 24)) % 365
years = (duration // (3600 * 24)) // 365

if 0 < duration < 60:
    print(f"{sec} сек")
elif 60 <= duration < 3600:
    print(f"{minutes} мин {sec} сек")
elif 3600 <= duration < (3600 * 24):
    print(f'{hours} час {minutes} мин {sec} сек')
elif (3600 * 24) <= duration < (3600 * 24 * 365):
    print(f" {days} дн {hours} час {minutes} мин {sec} сек")
else:
    print(f"{years}г. {days} дн {hours} час {minutes} мин {sec} сек")