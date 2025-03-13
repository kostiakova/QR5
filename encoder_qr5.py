# 5 colors:  black, white, red, green, cyan
# 5^3 = 125 (0-124 symbols in utf-8)
# quinary - кьинарное число

example_string = "Hello, world!"
dict_colors = {"0": "⚫", "1":"⚪", "2":"🟥", "3":"🟩", "4":"🟦", " ": " "}
# asserted_out_string = 

list_dict = {"b":0, "w":1, "r":2, "g":3, "c":4}
QuestionChar = '331'
SpaceChar = ' '

def utf8_to_quinary(string):
    def char_utf8_to_quinary(char):
        """
        Конвертирует символ UTF-8 в 5-ричное число.

        Args:
            char: Символ UTF-8.

        Returns:
            Строка, представляющая 5-ричное число.
        """
        if char == " ":
            return SpaceChar
        if char == "?":
            return QuestionChar
        quinary_value = []
        with open("list.json", "r") as json:
            for line in json.readlines():
                if char in line:
                    quinary_value.append(line.split(":")[0].replace("\"", "").replace("\"", ""))
        return ""+quinary_value[0]

    """
    converts a string into a list 
    of quinary symbols
    input -> string
    output -> list"""
    list_converted = []
    for character in string:
        list_converted.append(char_utf8_to_quinary(character))
    return list_converted

def quinary_to_utf8(list_q: list):

    def char_quinary_to_utf8(charr):
        """
        Конвертирует 5-ричное число в символ UTF-8.

        Args:
            char: Строка, представляющая 5-ричное число.

        Returns:
            Символ UTF-8.
        """
        if charr == "331":
            return "?"
        if charr == "332":
            return " "
        with open("list.json", "r") as json:
            for line in json.readlines():
                if charr in line:
                    sym_return = line.split(":")[1]
                    return sym_return[2]


    """Converts quinary sequience to UTF-8 encoding
    
    input->list of 0-4 symbols
    output-> string"""
    str_to_ret = ""
    if type(list_q) == list:
        for charr in list_q:
            str_to_ret += char_quinary_to_utf8(charr)
    elif type(list_q) == str:
        if "," in list_q:
            while " " in list_q:
                list_q = list_q.replace(" ", "")
            list_q = list_q.split(",")
            for charr in list_q:
                str_to_ret += char_quinary_to_utf8(charr)
        else: 
            list_q = list_q.split(" ")
            for charr in list_q:
                str_to_ret += char_quinary_to_utf8(charr)
        
    
    return str_to_ret

def quinary_to_colored_l(list_q: list):
    src_str = " ".join(str(el) for el in list_q)
    res_str = ""
    for chr in src_str:
        if chr == " ": res_str += " "
        else: res_str+= dict_colors[chr]
    return res_str


def quinary_to_colored_s(src_str: str):
    res_list = []
    sec_str = ""
    for chr in src_str:
        for number, color in dict_colors.items():
            if chr == color:
                sec_str+=number
                break
    
    res_list = sec_str.split(" ")
    return res_list

if __name__ == "__main__":
    # Usage Example      
    # quinary_to_utf8
    # utf8_to_quinary    
    # quinary_to_colored 
    # quinary_to_colored                                                                                        
    text = input("Enter text in english: ")
    quin = utf8_to_quinary(text)
    print(quin)
    print(quinary_to_utf8(quin))