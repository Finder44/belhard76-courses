text = input()
symbols = {i: text.count(i) for i in text}
print(symbols)
