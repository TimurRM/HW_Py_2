# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! 
# Реализовать свой метод


# from random import sample

# list = [1, 2, 3, 4, 5, 6]
 
# shuffled_list = sample(list, len(list))
# print(list)
# print(shuffled_list)


import random
def shaffle_list(my_list):
    list_1 = my_list[:]
    list_length = len(list_1)
    for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = list_1[i]
        list_1[i] = list_1[index]
        list_1[index] = temp
    return list_1
origin_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_list = shaffle_list(origin_list)
print(origin_list)
print(shuffled_list)

