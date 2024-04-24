# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3
numbs = input("Введите числа ")
list_numbs = numbs.split()
print(int(list_numbs[0])+int(list_numbs[1])+int(list_numbs[2]))
# если не с 3 числами
numbers = input()
summa= sum(map(int , numbers.split(' ')))
print(summa)
# split(' ')разделит все числа через пробел
# map(int) переводит числа в int
# sum() сума