# Заполнить список степенями числа 2 (от 2^1 до 2^n).
import math
numbers = int(input("Введите сьепенть числа 2 "))
g=0
degree = [pow(2, numbers) for i in range(1,numbers+2)]
print(degree)