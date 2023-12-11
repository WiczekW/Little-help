import linecache
def exp_class_from_uni(path_to_txt):
    # reading txt
    with open(path_to_txt, 'r') as file:
        temp_value = file.readline()
        temp_list = temp_value.split('§')
        #print(temp_list[18])

    # find path to uni
    path_to_uni = path_to_txt.replace('.txt', '_dec.uni')
    with open(path_to_uni, 'r', encoding='ANSI') as file:

        for i in range(25):
            line_from_uni = file.readline()
            if i==24:
                list_from_line = (line_from_uni.split())
            else:
                continue

    exp_uni = list_from_line[-1]
    #update exp class
    temp_list[18] = exp_uni
    # write new exp class to txt
    with open(path_to_txt, 'w') as file:
        final_line = str()
        for i in temp_list[:-1]:
            final_line += i+'§'
        file.write(final_line)

