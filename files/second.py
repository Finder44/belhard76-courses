def read_csv_to_dict_list(filename):
    # Открываем файл и читаем его строки
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()

    # Получаем заголовки колонок из первой строки
    headers = lines[0].split(',')

    data = []

    # Проходим по каждой строке, начиная со второй
    for line in lines[1:]:
        values = line.split(',')
        # Создаем словарь для текущей строки
        item = {headers[i]: values[i] for i in range(len(headers))}
        data.append(item)

    return data


filename = "newfile.csv"
data = read_csv_to_dict_list(filename)

for item in data:
    print(item)
