#калькулятор
num_1 = float(input("Введите 1 число "))
num_2 = int(input("Введите 2 число "))
print("Операции:(укажите цифру!)\n"
      "1. Сложение  +\n"
      "2. Разность  -\n"
      "3. Произведение  *\n"
      "4. Деление  /"
      )
operation = int(input("Укажите операцию "))
if operation == 1:
    print(num_1+num_2)
elif operation == 2:
    print(num_1 - num_2)
elif operation == 3:
    print(num_1 * num_2)
else:
    print(num_1 / num_2)