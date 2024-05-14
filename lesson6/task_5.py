numbers = [1, 2, 3, 4, 5]
length = len(numbers)


def new_reverse(numbers, length):
    for i in range(length // 2):
        numbers[i], numbers[length - i - 1] = numbers[length - i - 1], numbers[i]
    return numbers


print(new_reverse(numbers, length))
