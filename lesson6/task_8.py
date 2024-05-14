data = {
    "Ямайка": ["1", "2", "3", "4"],
    "Россия": ["11", "22", "33", "44"],
    "США": ["111", "222", "333", "444"]
}
your_city = input()


def city(your_city, data):
    for k, v in data.items():
        if your_city in v:
            return k


print(city(your_city, data))
