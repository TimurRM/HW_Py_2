# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! 
# Реализовать свой метод


# from random import sample

# list = [1, 2, 3, 4, 5, 6]
 
# shuffled_list = sample(list, len(list))
# print(list)
# print(shuffled_list)


import random
def shaffle_list(my_list):
    list = my_list[:]
    list_length = len(list)
    for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_list = shaffle_list(list)
print(list)
print(shuffled_list)

