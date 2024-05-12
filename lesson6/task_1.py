# Функция перевода чисел из 10 в 2 и наоборот
def to_sistem_10(walue):#разделить на 2 функции

    new_wal = []
    step = 0
    for i in str(walue):
        new_wal.append(int(i) * (2 ** int(step)))
        step+=1
    refe =0
    for i in new_wal:
        refe+= +i
    return refe

def to_sistem_2(walue):
    if walue > 0:
        # new_wal=[int(walue)%2for i in range(int(walue))]
        binary = ""
        while walue>0:
            remainder = walue%2
                # binary =str(remainder) + binary
            binary = f"{remainder}" + binary
            walue = walue//2
    else:
        binary = "0"
    return binary

walue = int(input("Введиет число "))
print(to_sistem_2(walue))
print(to_sistem_10(111))
    # print("".join(str(num) for num in new_wal))