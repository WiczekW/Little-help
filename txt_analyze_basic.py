import pandas as pd

attr_from_txt = ['name', 'status', 'quantity', 'conc_vol', 'steel_mass']


def read_txt(path):

    with open(path, 'r') as file:
        temp_txt = file.read()
        if temp_txt[0] == '§':
            temp_txt = temp_txt.split('§')
            temp_txt_ds = pd.Series(temp_txt)
            columns = attr_from_txt
            data_set = [temp_txt_ds[2], temp_txt_ds[22], temp_txt_ds[6], temp_txt_ds[7], temp_txt_ds[10]]

            #   check and convert 3 last values - string data to float
            data_set_types = []
            for i in data_set:
                data_set_types.append(isinstance(i, str))
            for i in range(2, 5):
                if data_set_types[i] == True:
                    data_set[i] = data_set[i].replace(',', '.')
                    data_set[i] = float(data_set[i])
                else:
                    continue

            #   creation of output data frame
            output = pd.DataFrame(columns=columns, data=[data_set])
            return output
        else:
            pass
