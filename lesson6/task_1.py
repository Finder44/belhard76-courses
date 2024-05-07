def new_sistem(walue,operation):
    if operation == 1:
        new_wal = []
        step = 0
        for i in str(walue):
            new_wal.append(int(i) * (2 ** int(step)))
            step+=1
        refe =0
        for i in new_wal:
            refe+= +i
        return refe

    else:
        # new_wal=[int(walue)%2for i in range(int(walue))]
        binary = ""
        while walue>0:
            remainder = walue%2
            binary +=str(remainder)
            walue = walue//2
        return binary

walue = int(input("Введиет число "))
operation = int(input("Выберите операцию "))

print(new_sistem(walue,operation))
    # print("".join(str(num) for num in new_wal))