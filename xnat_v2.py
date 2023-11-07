import numpy as np
import glob as gb
from func_xnat_v2 import xlsx_to_df, xlxs_rebar_to_df, explode_abs_to_df
import pandas as pd
import template_txt

pd.options.display.max_columns = 150
pd.options.display.max_colwidth = 150


def df_integration(path_folder):

    path1 =f'{path_folder}/txt_att_v1.xlsx'
    path3 =f'{path_folder}/txt_zbr_v2.xlsx'
    df_attr = xlsx_to_df(path1)
    df_rebar_xlsx = xlxs_rebar_to_df(path3)
    df_integrated = df_attr

    # first marge with attributes
    df_final = pd.merge(template_txt.df_empty, df_integrated.rename(columns = template_txt.keys_to_columns_inv), how='outer')
    df_final.set_index('L_key', inplace=True)

    # fill nan values
    df_final.fillna(inplace=True, value=0)

    try:
        # add steel to df_final
        rebar_from_df = df_rebar_xlsx.values.tolist()


        for i in rebar_from_df:
            str_layer = int(str((i[0])).split('.')[0])
            str_diam = 'd' + str((i[2])).split('.')[0] + ' mass'
            str_diam = template_txt.keys_to_columns_inv[str_diam]
            mass_bar = i[3] * i[5]
            df_final.at[str_layer, str_diam] = df_final.at[str_layer, str_diam] + mass_bar

    except KeyError:
        print('Nie wykryto zbrojenia')

    # edition of values in df_final

    df_final['G'] = df_final['A']

    value_to_l = df_final['L']
    value_to_l = value_to_l + '|' + df_final['M'].astype('str') \
                 + '|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-'
    df_final['L'] = value_to_l

    df_final['REV'] = '$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$' \
                      ' $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$ $$|$'
    try:
        df_final['E'] = df_final['G'].apply(lambda row: row.split('_')[0])
    except AttributeError:
        print(f'Nie wczytano nazwy')
    df_final.replace(to_replace=template_txt.keys_to_name, inplace=True)

    # overwite dimensions if neccessary
    little_list = ['X-overwrite', 'Y-overwrite', 'Z-overwrite']
    little_list2 = ['AJ', 'AK', 'AL']
    little_list3 = ['X-transport', 'Y-transport', 'Z-transport']
    little_list4 = ['D10', 'D11', 'D12']

    for source_col,target_column in zip(little_list, little_list2):
        filtrating_obj = df_final[source_col] != 0
        df_final.loc[filtrating_obj, target_column] = df_final.loc[filtrating_obj, source_col]

    for source_col, target_column, target_column_key in zip(little_list2, little_list3, little_list4):
        filtrating_obj = df_final[target_column] == 0
        df_final.loc[filtrating_obj, target_column] = df_final.loc[filtrating_obj, source_col]
        df_final.loc[:,target_column_key] = df_final.loc[:,target_column]


    return df_final[template_txt.columns_of_txt]




def row_to_txt(df_xnat, path_save):
    result = df_xnat.apply(lambda y: y.tolist(), axis=1)
    result_list = result.to_list()
    list_joined = []

    for i in result_list:
        converted_i = [str(element) for element in i]
        joined_i = '§' + '§'.join(converted_i) + '§'
        list_joined.append(joined_i)
    list_to_export = []
    for j in list_joined:
        temp = [result_list[list_joined.index(j)][1] + '.txt', j]
        list_to_export.append(temp)

    for k in list_to_export:
        temp_path = path_save + '\\' + k[0]
        with open(temp_path, mode='w', encoding='ANSI') as file:
            file.write(k[1])



#x=df_integration(path)
#print(x)
#print(row_to_txt(x, path9))











