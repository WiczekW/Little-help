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
            for i in range(500):
                single_line = temp_file.readline()
                temp_uni.append(single_line)
            unis_encrypted.append(temp_uni)


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
                unis_acc[index_of_j]=j[:index_of_end]
                break
            else:
                continue
    # find lines with acc and numbers and save it to tuple
    for g in unis_acc:
        uni_acc_counted = list()
        for line in g:
            if '            ' in line:
                index_of_name = g.index(line)
                index_of_nr = g.index(line) + 2
                clear_line = line.replace('\n', '')
                splitted_line = clear_line.split('            ')
                acc_name = splitted_line[1]
                acc_number = g[index_of_nr]
                acc_number_cleared = acc_number.replace('\n', '').replace(' ', '')
                # delete mistakes by counting tuple(1)
                if len(acc_number_cleared) != 12:
                    continue
                key_acc = [acc_name, acc_number_cleared, 1]
                # add key_acc to uni_acc_counted and check is it already there
                if len(uni_acc_counted) == 0:
                    uni_acc_counted.append(key_acc)
                else:
                    is_in = []
                    for k in uni_acc_counted:
                        if k[1] == key_acc[1]:
                            is_in.append(True)
                        else:
                            is_in.append(False)
                    if len(is_in) == is_in.count(False):
                        uni_acc_counted.append(key_acc)
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
    print(unis_acc_counted)
    print(uni_names)

    # write acc to txt files
    txt_paths = list()
    for i in uni_paths:
        txt_paths.append(i.replace('uni', 'txt'))

    try:
        for j in txt_paths:
            with open(j, 'w') as file:
                temp_file = file
                for k in uni_names:
                    if k in j:
                        ix = uni_names.index(k)
                        str_to_write = unis_acc_counted[ix][2]+ '§' + \
                                       unis_acc_counted[ix][0]+ '§' + \
                                       unis_acc_counted[ix][1]
                        print(str_to_write)
                        file.write(str_to_write)

                    else:
                        continue

    except:
        pass



acc_uni_to_txt("C:\\Users\\wiktor.gajewski\\Desktop\\!bum\\testowe")


