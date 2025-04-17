import encoder_qr5V2 as enc

dict_colors = {0: "⚫", 1:"⚪", 2:"🟥", 3:"🟩", 4:"🟦"}
reversed_colors = {"⚫": 0, "⚪":1, "🟥":2, "🟩":3, "🟦":4}

def quin_to_color(src: list) -> list:
    r = []
    t = ""
    for el in src:
        s = str(el)
        for char in s:
            t += dict_colors[int(char)]
        r.append(t)
        t = ""
    return r

def color_to_quin(src: list) -> list:
    r = []
    t = ""
    for el in src:
        s = str(el)
        for char in s:
            t += str(reversed_colors[char])
        r.append(int(t))
        t = ""
    return r

x = enc.list_quinary(enc.get_utf_code("privetc kaak del?|||"))
print(x)
print(quin_to_color(x))
v = color_to_quin(quin_to_color(x))
print(v)
print(enc.list_decimal(v))
print(enc.get_char_from_code(enc.list_decimal(v)))