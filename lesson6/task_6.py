numbers = [1, 2, 4, 6, 65, 3, 0, 22, 1, 23, 12, 3, 12, 4, 35, 2]
even = []
numb = []
zero_elem = []


def sum(numbers, even=[], numb=[], zero_elem=[]):
    for number in numbers:
        if number % 2:
            numb.append(number)
        elif number == 0:
            zero_elem.append(number)
        else:
            even.append(number)
    return even + zero_elem + numb


print(sum(numbers))
