# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
data = {
    i: {
        "name": input(f"name {i}="),  # 3
        "emaeil": input((f"email {i}="))  # 3
    }
    for i in range(1, int(input("n=")) + 1)  # 1
}
print(data)
# РАЗБЕРИСЬ разберись
# n = input()
# data = {
#     i:{
#         "name":input(f"name {i} " ),
#         "email":input(f"email {i}")
#     }
#     for i in range(1, int(n)+1)
# }
# print(data)
# for неусловный,перебор
# while условный