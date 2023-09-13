import pandas as pd
import os


attr_from_txt_ext = ['project', 'name', 'timestamp', 'status', 'quantity',
                     'element_type', 'volume', 'conc', 'steel_mass', 'X-dim', 'Y-dim',
                     'Z-dim', 'exposure', 'fire resistance', 'strands_bottom', 'strands_top'
                     ]


def read_txt_extended(path):

    with open(path, 'r') as file:
        temp_txt = file.read()
        if temp_txt[0] == '§':
            temp_txt = temp_txt.split('§')
            temp_txt_ds = pd.Series(temp_txt)
            columns = attr_from_txt_ext
            data_set = [temp_txt_ds[66], temp_txt_ds[2], os.path.getctime(path), temp_txt_ds[22], temp_txt_ds[6],
                        temp_txt_ds[63], temp_txt_ds[7], temp_txt_ds[8], temp_txt_ds[10], temp_txt_ds[19],
                        temp_txt_ds[20], temp_txt_ds[21], temp_txt_ds[18], temp_txt_ds[17], temp_txt_ds[11],
                        temp_txt_ds[14]
                        ]

            #   creation of output data frame
            output = pd.DataFrame(columns=columns, data=[data_set])

            #   correcting types of data
            columns_to_correct = ['quantity', 'volume', 'steel_mass', 'X-dim',
                                  'Y-dim', 'Z-dim', 'strands_bottom', 'strands_top']

            for column in columns_to_correct:
                output[column] = output[column].str.replace('-', '0')
                output[column] = output[column].str.replace(',', '.')
                try:
                    output[column] = output[column].astype('float')
                except ValueError:
                    continue

            return output
        else:
            pass
#link = '\\\\dp.pekabex.poznan\\projekty2021\\PHGN - PW HALE Wital Goldap\\Na produkcje\\2021-03-15_IVF_01S\\IVF_01S.txt'
#link = '\\\\dp.pekabex.poznan\\projekty2021\\PHGN - PW HALE Wital Goldap\\Na produkcje\\2021-03-17_IVF_01Z\\IVF_01Z.txt'
#print(read_txt_extended(link))
