import openpyxl
import mass_to_dict_v1
import dim_correction


def txt_gen(excel_path_from_gui):
#   input of excel path
    excel_path = str(excel_path_from_gui)
#   adjusting path of file
    excel_path = excel_path.replace('"', '')

#   abs path from excel path
    abs_location = excel_path
    while abs_location[-1] != '/':
         abs_location = abs_location[:-1]


#   load of excel file
    excel = openpyxl.load_workbook(excel_path)
    arkusz = excel['txt_allplan_v17_S_czysty']

#   input data to excel
    first_row = 3
    base = list()
    z = '§'

#   import data from excel
    while arkusz.cell(row=first_row, column=1).value == '§':
        imported_row = list(arkusz.rows)[first_row-1]
    #   from tuple to list
        imported_row_list = []
        for item in imported_row:
            item_converted = item.value
            imported_row_list.append(item_converted)
        
        base.append(imported_row_list)
        print('wiersz nr', first_row, 'wczytany')
        first_row += 1
  
#   add mass of steel
    for element in base:
        try:
         
            rebar_by_diameter = mass_to_dict_v1.mass_to_dict((abs_location+element[3]))
            element[19] = rebar_by_diameter['total']
            element[131] = rebar_by_diameter[4]
            element[133] = rebar_by_diameter[5]
            element[135] = rebar_by_diameter[6]
            element[137] = rebar_by_diameter[8]
            element[139] = rebar_by_diameter[10]
            element[141] = rebar_by_diameter[12]
            element[143] = rebar_by_diameter[14]
            element[145] = rebar_by_diameter[16]
            element[147] = rebar_by_diameter[18]
            element[149] = rebar_by_diameter[20]
            element[151] = rebar_by_diameter[22]
            element[153] = rebar_by_diameter[25]
            element[155] = rebar_by_diameter[28]
            element[157] = rebar_by_diameter[32]
            element[159] = rebar_by_diameter[40]
            element[161] = rebar_by_diameter[42]
            element[163] = rebar_by_diameter[45]
            print('Masa stali wczytana dla ', str(element[3]))
        except FileNotFoundError:
            print('Nie udało się wczytać mas zbrojenia z plików ABS dla ', str(element[3]),
                  '''Upewnij się, że są w tym samym folderze co excel.''')

    #   dim correction
    types_to_correct = ['belka zbrojona szalunek', 'sciana pelna szalunek', 'sciana 3 warstwowa szalunek']

    for element in base:
        if element[299] in types_to_correct:

            #   tuple generator (length, width, height) width - smallest, length - biggest
            dimensions_tuple = dim_correction.dim_correction(element)

            element[37] = dimensions_tuple[0]
            element[39] = dimensions_tuple[1]
            element[41] = dimensions_tuple[2]

            print('Poprawiono wymiary w ', str(element[3]))

    #   clear of the old txt files
    for element in base:
        name_of_element = str(element[3])
        name_of_txt = name_of_element + '.txt'
        path_of_txt = abs_location + name_of_txt
        with open(path_of_txt, 'w', encoding='ANSI') as file:
            file.write('')

    #   base crated as string
    base_converted = []


    #   change all to string and replace , with . and save to base converted

    for element in base:
        element_list = []

        for var in element:
            var = str(var)
            var = var.replace('.', ',')
            element_list.append(var)

        base_converted.append(element_list)

    #   creation of txt files
    for element in base_converted:
        print('Generowanie TXT dla ' + str(element[3]))
        for var in element:
            name_of_element = str(element[3])
            name_of_txt = name_of_element + '.txt'
            path_of_txt = abs_location + name_of_txt
            with open(path_of_txt, 'a+', encoding='ANSI') as file:
                file.write(var)

    print('Pliki TXT wygenerowane')

