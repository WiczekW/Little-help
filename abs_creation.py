from xnat_v2 import df_integration
from func_xnat_v2 import xlsx_to_df,explode_abs_to_df,xlxs_rebar_to_df

path6 = 'C:\\Users\\wiktor.gajewski\\Desktop\\!bum\\DZIS'



def abs_creation(df_from_integration, main_path):
    df_attr = df_from_integration
    path_to_abs = f'{main_path}\\to_explode.abs'
    path_to_rebar = f'{main_path}'\\txt
    df_abs_integ = explode_abs_to_df(f'{main_path}\\to_explode.abs')

    df_rebar_xlsx = xlxs_rebar_to_df(path9)
    print(df_attr)



    list_of_columns_attry = df_attr.columns.tolist().remove(0)
    #print(list_of_columns_attry)
    df_to_single_abs = df_attr.drop(labels=[list_of_columns_attry], axis='columns')
    #print(df_to_single_abs)


x = df_integration(path6)
y = abs_creation(x, path6)
