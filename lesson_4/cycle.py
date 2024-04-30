# Заполнить список степенями числа 2 (от 2^1 до 2^n).
numbers = int(input("Введите сьепенть числа 2 "))
degree = [2 ** i for i in range(1,numbers+1)]
print(degree)