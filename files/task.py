def findLength(string):
    # Initialize count to zero
    count = 0

    # Counting character in a string
    for i in string:
        count += 1
    # Returning count
    return count
file = open("first.yaml", "r", encoding='utf-8')
all_lines = file
col_words = 0
for line in all_lines:
    print(f"Длинна строки {findLength(line)}")
file.close()



