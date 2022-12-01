# Задайте список из n чисел последовательности (1 + 1/n)^n. 
# Вывестив консоль сам список и сумму его элементов.


def my_list(num): 
    mainList = []
    for i in range(1, num + 1):
        mainList.append(round((1+1/i)**i,3))
    return mainList

number = int(input('Введите число: '))
result = my_list(number)

def sumOfMylist(result):
    sum = 0
    for i in range(len(result)):
        sum += result[i]
    return sum
 


print(f'My list: {my_list(number)}')
print(f'Summ: {sumOfMylist(result)}')

