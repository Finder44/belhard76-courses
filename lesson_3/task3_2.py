# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3
numbs = input("Введите числа ")
list_numbs = numbs.split()
full = (int(list_numbs[0]) + int(list_numbs[1]) + int(list_numbs[2])) / 3
print(round(full, 3))
# если не с 3 числами
numbers = input()
numbers_list = list(map(int, numbers.split(' ')))
count = len(numbers_list)
# print(count)
summa = sum(map(int, numbers.split(' ')))
print(round(summa / count))
# split(' ')разделит все числа через пробел
# map(int) переводит числа в int
# sum() сума
# count = len(numbers_list) len считает длинну по индексам
