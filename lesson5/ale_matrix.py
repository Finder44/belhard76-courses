#Вывеси четные числа от 2 до N по 5 в строку

n = int(input("Введите конечну гарницу "))
ww = 0
for i in range(2,n):
    print( i, end=' ')
    ww+=1
    if not(ww % 5):
        print()