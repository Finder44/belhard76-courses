numb_1 = int(input("Введите первое число "))
numb_2 = int(input("Введите второе число "))
numb_3 = int(input("Введите третье число "))
positive = (numb_1 > 0) + (numb_2 > 0) + (numb_3 > 0)
negative = (numb_1 < 0) + (numb_2 < 0) + (numb_3 < 0)
print("Вы ввели", positive, "положительных чисел и", negative, "отрицательных")
# bool принимет 0 или 1 что и дает возможность счета 5 2 10 (1+1+1)