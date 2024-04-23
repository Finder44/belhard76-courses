# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами
text = input("Введите сообщение ")
print(text.replace(" ", "-"))
list_text = text.split()
new_text = "-".join(list_text)
print(new_text)

