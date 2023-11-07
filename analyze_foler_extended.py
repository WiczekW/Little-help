import pandas as pd
from txt_analyze_extended import read_txt_extended, attr_from_txt_ext
from Look_for_path import Look_for_prj
import openpyxl
import tkinter as tk


def c2_folder_extended(chosen_path):

    analyzed_folder = Look_for_prj()

    data_to_excel = pd.DataFrame(columns=attr_from_txt_ext)

    txt_list = analyzed_folder.search_txt_selected_folder(chosen_path)
    for txt in txt_list:
        print(txt)
        new_elem = read_txt_extended(txt)
        try:
            filter_obj = data_to_excel['name'] != new_elem.iloc[0, 1]
            data_to_excel = data_to_excel[filter_obj]
            data_to_excel = data_to_excel.merge(new_elem, how='outer')
        except ValueError:
            print('ValueError: ', 'Zignorowano plik txt')
            continue
        except AttributeError:
            print('AttributeError: ', 'Zignorowano plik txt')
            continue


    #   postproduction of data
    data_to_excel['conc_vol_global'] = data_to_excel['volume']*data_to_excel['quantity']
    data_to_excel['steel_mass_global'] = data_to_excel['steel_mass'] * data_to_excel['quantity']
    data_to_excel['kg/m3'] = data_to_excel['steel_mass']/data_to_excel['volume']
    data_to_excel['mass'] = data_to_excel['volume'] * 2500
    data_to_excel['assembly mass'] = data_to_excel['mass'] * 1.15
    data_to_excel.sort_values(['name'], inplace=True)

    list_of_columns = ['project', 'name', 'quantity', 'volume', 'steel_mass', 'kg/m3',
                       'conc_vol_global', 'mass', 'assembly mass', 'steel_mass_global',
                       'X-dim', 'Y-dim', 'Z-dim', 'status', 'conc', 'exposure', 'fire resistance',
                       'strands_bottom', 'strands_top'
                       ]

    data_to_excel[list_of_columns].to_excel('Data_from_txt - CUSTOM ' + '.xlsx')
    print('Utworzono plik excel')


