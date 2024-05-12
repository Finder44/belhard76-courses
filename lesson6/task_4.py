text = ["man" ,2 ,2 ,4, 5, " alfa " , "bet"]
text = list(filter(lambda x: isinstance(x,str), text))
print(text)

mixed_list = [1, "apple", 3.14, True, "banana", None, "cherry", False, "date"]

filtered_list = [x for x in mixed_list if isinstance(x, str)]

print(filtered_list)

for index in range(len(text)):
    if not isinstance(text[index],str):
        text.pop(index)
print(text)