def sum_neighbors(numbers):
    new_numbs = []
    length = len(numbers)
    for i in range(length):
        prev_index = (i - 1) % length  # Предыдущий элемент (циклический индекс)
        next_index = (i + 1) % length  # Следующий элемент (циклический индекс)
        new_numbs.append(numbers[prev_index] + numbers[i] + numbers[next_index])
    return new_numbs

numbers = [1, 23, 3, 454, 5, 4, 2, 2, 3, 2, 1, 6, 7, 8, 5, 3, 2, 234]
print(sum_neighbors(numbers))
