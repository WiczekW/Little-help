import pandas as pd
import glob as gb
from template_txt import columns_of_txt


def xlsx_to_df(path):
    imported_xlsx = pd.read_excel(path, header=1, usecols=[i for i in range(1, 40)])
    #imported_xlsx.set_index(['L_key'], inplace=True)
    return imported_xlsx

def explode_abs_to_df(path):

    splitted_i_core = []
    with open(path, 'r') as file:
        integrated_abs = file.readlines()
        ds_integrated = pd.Series(integrated_abs)

        for i in ds_integrated:
            splitted_i = i.split('@')[4:10]
            splitted_i_bar = []
            for j in splitted_i:
                splitted_i_bar.append(j[1:])
            splitted_i_core.append(splitted_i_bar)


    integrated_df = pd.DataFrame(splitted_i_core, columns=['Bar number', 'Bar length', 'Bar quantity', 'Bar weight', 'Bar diameter', 'Bar steel'])
    integrated_df['line_to_abs'] = ds_integrated
    return integrated_df
def xlxs_rebar_to_df(path):
    imported_xlsx_df = pd.read_excel(path, header=3, usecols=[i for i in range(6)])
    return imported_xlsx_df









#x = xlsx_to_df('C:\\Users\\wiktor.gajewski\\Desktop\\!bum\\DZIS\\txt_test_v3.xlsx')
#print x
#y = explode_abs('C:\\Users\\wiktor.gajewski\\Desktop\\!bum\\DZIS\\TXT.abs')
#print(y[['Bar number', 'Bar length', 'Bar quantity', 'Bar weight', 'Bar diameter', 'Bar steel']])
#z = xlxs_rebar_to_df('C:\\Users\\wiktor.gajewski\\Desktop\\!bum\\DZIS\\txt_zbr_v1.xlsx')
#print(z)

#filter = []
#filter = y.duplicated().tolist()
#print(y[filer])

