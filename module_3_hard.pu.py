def custom_write(file_name, strings):
    the = {}
    with open(file_name, "r", encoding="utf-8") as file:
        a = file.read().split("\n")
    stroka = len(a)
    with open(file_name, "a", encoding="utf-8") as file:
        for i in strings:
            a = file.tell()
            file.write(f"{i}\n")
            the[(stroka, a)] = i
            stroka += 1
    return the