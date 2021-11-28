# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for number in range(1, 101):
    last_digit = number % 10

    if last_digit == 1:
        print(f"{number} процент")
    elif last_digit in range(2, 5):
        print(f"{number} процента")
    else:
        print(f"{number} процентов")