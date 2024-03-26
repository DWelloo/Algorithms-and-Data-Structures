def find(string, text):
    if len(string) == 0:
        return []
    if len(string) > len(text):
        return []
    indexes = []
    anchor = 0
    first = True
    str_i = 0
    txt_i = 0
    while txt_i < len(text):
        if len(string) == 1:
            str_i = 0
            first = False
            anchor = txt_i
        if string[str_i] == text[txt_i]:
            if first:
                anchor = txt_i
                first = False
            elif str_i + 1 == len(string):
                indexes.append(anchor)
                first = True
                str_i = -1
            str_i += 1
        else:
            if not first:
                txt_i = anchor
                first = True
            str_i = 0
        txt_i += 1
    return indexes


if __name__ == '__main__':
    text = "ALA MA MAŁEGO KOTA. MAŁEGO"
    string = "MAŁEGO"
    print(find(string, text))