# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11



def digitSum(inputedValue):
    sum = 0
    for i in str(inputedValue):
        if i != "." and i != "-":
            sum += int(i)
    return sum

value = input("Введите число: ")


print(f"{value} -> {digitSum(value)}")




