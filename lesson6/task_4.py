text = ["man", 2, 2, 4, 5, " alfa ", "bet"]
text = list(filter(lambda x: isinstance(x, str), text))
print(text)

mixed_list = [1, "apple", 3.14, True, "banana", None, "cherry", False, "date"]


def filter2(mixed_list):
    filtered_list = [x for x in mixed_list if isinstance(x, str)]
    return filtered_list


def filter3(text):
    for index in range(len(text)):
        if not isinstance(text[index], str):
            text.pop(index)
    return text


print(filter2(mixed_list))
print(filter3(text))
