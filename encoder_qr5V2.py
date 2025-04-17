EX__STR = "Wie heist du? This is problem! ce n'est pas le problem pour moi|"
ret_s = []
dict_colors = {0: "⚫", 1:"⚪", 2:"🟥", 3:"🟩", 4:"🟦"}
reversed_colors = {"⚫": 0, "⚪":1, "🟥":2, "🟩":3, "🟦":4}

def str_to_list(src: str):
    return list(src)

def lst_to_str(src: list):
    return "".join(src)

def dec_to_quin(decimal):
    res = ""
    while decimal >= 1:    # Should be >= 1, not > 1.
        res = str(decimal%5) + res
        decimal //= 5
    return int(res)

def quin_to_dec(num):
    decimal_value = 0
    base = 1
    while (num):
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 5
    return decimal_value

def get_utf_code(string: str) -> list:
    lst = str_to_list(string)
    ret_s = []
    for i in range(len(lst)):
        ret_s.append(ord(lst[i]))
    return ret_s

def get_char_from_code(codees: list) -> str:
    return lst_to_str([chr(i) for i in codees])

def list_quinary(list_: list) -> list:
    return [dec_to_quin(i) for i in list_]
def list_decimal(list_q) -> list:
    return [quin_to_dec(i) for i in list_q]

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

def str_to_quin(src: str) -> list:
    return list_quinary(get_utf_code(src))

def str_to_colored(src: str) -> list:
    return quin_to_color(list_quinary(get_utf_code(src)))

def colored_to_str(src: list) -> str:
    return get_char_from_code(list_decimal(color_to_quin(src)))

def quin_to_str(src: list) -> str:
    return get_char_from_code(list_decimal(src))
# EXAMPLE: 
# quin = list_quinary(get_utf_code(EX__STR))
# colors = quin_to_color(quin)
# quin = color_to_quin(colors)
# dec = list_decimal(quin)
# strr = get_char_from_code(dec)
# print(str_to_quin(EX__STR))
# print(str_to_colored((EX__STR)))
# print(colored_to_str(['🟥🟦🟥', '🟦⚫⚪', '🟦⚪🟩', '🟦⚪🟩', '🟦🟥⚪', '⚪⚪🟥', '⚪🟦🟦', '🟩🟩⚫']))
# print(quin_to_str([322, 410, 401, 112, 404, 401]))