numbers = [1, 23, 3, 454, 5, 4, 2, 2, 3, 2, 1, 6, 7, 8, 5, 3, 2, 234]
finish = len(numbers) - 1  # c 0
last = numbers[-1]
print(finish)
def sum(numbers,finish,last):
    step = 0
    new_numbs = []
    for i in range(finish):
        # prev_index=
        # next_index=
        new_numbs.append(numbers[i - 1] + numbers[i] + numbers[i + 1])
        if i == finish:
            new_numbs.append(numbers[i - 1] + numbers[i] + numbers[0])
    return new_numbs
print(sum(numbers,finish,last))#узнать про последний элемент