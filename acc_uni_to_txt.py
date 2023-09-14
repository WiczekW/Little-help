import glob as gb


def acc_uni_to_txt(chosen_path):
    path_to_glob_uni = chosen_path+'\\*.uni'
    uni_paths = gb.glob(path_to_glob_uni)
    unis_encrypted = list()
    unis_acc = list()
    uni_names = list()
    unis_acc_counted = []

    # get files to the list uni_encrytped files
    for path in uni_paths:
        with open(path, mode='r') as file:
            temp_file = file
            temp_uni = list()
            # read line by line 500 lines and save it to temp_uni
            try:
                for i in range(1500):
                    single_line = temp_file.readline()
                    temp_uni.append(single_line)
                unis_encrypted.append(temp_uni)
            except UnicodeDecodeError:
                print('WYJATEK, nie wczytano :', path)
                continue

    # remove lines before MOUNPART and save UNIS_ACC
    for i in unis_encrypted:
        uni_acc = i
        for line in uni_acc:
            if line[0:8] == 'MOUNPART':
                uni_acc = uni_acc[1:]
                break
            else:
                uni_acc = uni_acc[1:]
        unis_acc.append(uni_acc)

    # remove lines after END
    for j in unis_acc:
        for line in j:
            if line[0:3] == 'END':
                index_of_end = j.index(line)
                index_of_j = unis_acc.index(j)
                unis_acc[index_of_j] = j[:index_of_end]
                break
            else:
                continue
    # find lines with acc and numbers and save it to tuple
    for g in unis_acc:
        uni_acc_counted = list()
        for line in g:
            if '            ' in line:
                index_of_nr = g.index(line) + 2
                clear_line = line.replace('\n', '')
                splitted_line = clear_line.split('            ')
                acc_name = splitted_line[1]
                acc_name = acc_name.replace('©', 'e')
                acc_name = acc_name.replace('ť', 'l')
                acc_number = g[index_of_nr]
                acc_number_cleared = acc_number.replace('\n', '').replace(' ', '')
                # delete mistakes by counting tuple(1)
                key_acc = [acc_name, acc_number_cleared, 1]
                if len(acc_number_cleared) != 12:
                    if len(acc_number_cleared) != 0:
                        continue

                # add key_acc to uni_acc_counted and check is it already there
                if len(uni_acc_counted) == 0:
                    uni_acc_counted.append(key_acc)
                else:
                    is_in = []
                    # countin accs with number
                    for k in uni_acc_counted:
                        if k[0] == key_acc[0]:
                            is_in.append(True)
                        else:
                            is_in.append(False)
                    if len(is_in) == is_in.count(False):
                        uni_acc_counted.append(key_acc)
                    elif k[1] == '':
                        continue
                    else:
                        index_of_exist_acc = is_in.index(True)
                        uni_acc_counted[index_of_exist_acc][2] += 1

            else:
                continue
        unis_acc_counted.append(uni_acc_counted)

    # find names of elements and save to uni_names
    for i in unis_encrypted:
        line_name = i[21]
        line_name_splitted = line_name.split(' ')
        name_elem = line_name_splitted[0]
        uni_names.append(name_elem)

    # write acc to txt files
    txt_paths = list()

    for i in uni_names:
        path_to_txt = path_to_glob_uni.replace('*.uni', i + '.txt')
        txt_paths.append(path_to_txt)

    for i in txt_paths:
        s = '§'
        list_to_write = unis_acc_counted[txt_paths.index(i)]
        for j in list_to_write:
            str_to_write = '\n'+str(j[2])+s+j[0]+s+s+j[1]
            with open(i, 'a', encoding='ANSI') as file:
                file.write(str_to_write)

    # add girders to txt
    unis_girder = list()
    # remove lines before BRGIRDER and save unis_girder
    for i in unis_encrypted:
        uni_girder = i
        for line in uni_girder:
            if line[0:8] == 'BRGIRDER':
                uni_girder = uni_girder[1:]
                break
            else:
                uni_girder = uni_girder[1:]
        unis_girder.append(uni_girder)

    # remove lines after END
    for j in unis_girder:
        for line in j:
            if line[0:3] == 'END':
                index_of_end = j.index(line)
                index_of_j = unis_girder.index(j)
                unis_girder[index_of_j] = j[:index_of_end]
                break
            else:
                continue

    unis_girder_counted = []

    #counting girders in unitechnik
    for i in unis_girder:
        uni_girder_counted = []
        for j in i:
            if len(j) == 59:
                is_in_gird = []
                girder_line = j.split(' ')
                girder_list = [girder_line[3], girder_line[4], 1]
                if len(uni_girder_counted) == 0:
                    uni_girder_counted.append(girder_list)
                else:
                    for k in uni_girder_counted:
                        if k[0] == girder_list[0] and k[1] == girder_list[1]:
                            is_in_gird.append(True)
                        else:
                            is_in_gird.append(False)
                    if len(is_in_gird) == is_in_gird.count(False):
                        uni_girder_counted.append(girder_list)
                    else:
                        index_of_exist_gird = is_in_gird.index(True)
                        uni_girder_counted[index_of_exist_gird][2] += 1
        unis_girder_counted.append(uni_girder_counted)

    #write girders to txt file

    for i in txt_paths:
        s = '§'
        list_to_write = unis_girder_counted[txt_paths.index(i)]
        for j in list_to_write:
            str_to_write = '\n'+str(j[2])+s+j[0]+s+j[1]+s+s
            with open(i, 'a', encoding='ANSI') as file:
                file.write(str_to_write)






#acc_uni_to_txt("C:\\Users\\wiktor.gajewski\\Desktop\\!bum\\testowe")

