with open("list_chars.txt", "r") as f:
    lines = f.readlines()
    with open("list.json", "a") as fil:
        for i in range(len(lines)):
            lst = list(lines[i])
            lst.insert(0, "\"")
            lst.insert(4, "\"")
            fil.write("".join(str(sym) for sym in lst))