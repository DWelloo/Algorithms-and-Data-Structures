def find(string,text):
    l_string=len(string)
    if l_string == 0:
        return []
    l_text=len(text)
    if l_string > l_text:
        return []
    indexes = []
    table = table_KMP(string)
    anchor = 0
    first = True
    str_i = 0
    txt_i = 0
    while txt_i < l_text:
        if l_string == 1:
            str_i = 0
            first = False
            anchor = txt_i
        if string[str_i] == text[txt_i]:
            if first:
                anchor = txt_i
                first = False
            elif str_i + 1 == l_string:
                indexes.append(anchor)
                first = True
                str_i = -1
            str_i += 1
        else:
            if table[str_i] == -1:
                if not first:
                    txt_i = anchor
                    first = True
                str_i = 0
            else:
                anchor = txt_i - table[str_i]
                txt_i -= 1
                str_i = table[str_i]
                if str_i == 0:
                    first = True
        txt_i += 1
    return indexes


def table_KMP(string):
    table = [-1]
    i_compare = 0
    width = 0
    l_string=len(string)
    for i in range(1, l_string + 1):
        if i < l_string and string[i_compare] == string[i]:
            table.append(table[width])
            width += 1
            i_compare += 1
        else:
            table.append(width)
            width = 0
            i_compare = 0
            if i < l_string and string[i_compare] == string[i]:
                width += 1
                i_compare += 1
    return table


if __name__ == '__main__':
    text = "ALA MA MAŁEGO KOTA. MAŁEGO"
    string = "MAŁEGO"
    print(find(string, text))
