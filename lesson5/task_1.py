# Вывести первые N чисел кратные M и больше K
start = int(input("Введите начальную границу "))
stop=int(input("Задайте конечную границу "))
coll = int(input("Сколько чисел вывести "))
multiplicity = int(input("Введите какому числу должны быть кратны числа "))
stoper = 0
for i in range(start,stop ):
    if not (i % multiplicity):
        if stoper != coll:
            print(i)
            stoper+=1

