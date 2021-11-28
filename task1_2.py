# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
cube_list = []
for number in range(1, 1000, 2):
    number = number ** 3
    cube_list.append(number)
print(cube_list)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
total = 0
for number in cube_list:
    digit_sum = 0
    temp_number = number
    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number = temp_number // 10
    if digit_sum % 7 == 0:
        total += number
print(total)

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
# нацело на 7.
for number in range(len(cube_list)):
    cube_list[number] += 17
print(cube_list)

total = 0
for number in cube_list:
    digit_sum = 0
    temp_number = number
    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number = temp_number // 10
    if digit_sum % 7 == 0:
        total += number
print(total)