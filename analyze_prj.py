import pandas as pd
from txt_analyze_basic import read_txt, attr_from_txt
from Look_for_path import Look_for_prj
import openpyxl

def c2_prj():

    shortcut = input('Wpisz skrót kontraktu - ')

    analyzed_prj = Look_for_prj()
    analyzed_prj.single_prj(shortcut)

    data_to_excel = pd.DataFrame(columns=attr_from_txt)

    txt_list = analyzed_prj.search_txt()
    for txt in txt_list:
        print(txt)
        new_elem = read_txt(txt)
        try:
            data_to_excel = data_to_excel[data_to_excel['name'] != new_elem.iloc[0, 0]]
            data_to_excel = data_to_excel.merge(new_elem, how='outer')
        except ValueError and AttributeError:
            print('Zignorowano plik txt' )
            continue
    data_to_excel['conc_vol'] = data_to_excel['conc_vol'] * data_to_excel['quantity']
    data_to_excel['steel_mass'] = data_to_excel['steel_mass'] * data_to_excel['quantity']

    data_to_excel.to_excel('C2_filler -' + shortcut + '.xlsx')
    print('Utworzono plik excel')



