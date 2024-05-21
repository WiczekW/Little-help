import glob as gb
from Production_analyzer.is_txt_oneline import is_empty_acc
import os
import openpyxl
import pandas as pd
import re


chosen_path = "C:\\Users\\Wik\\Desktop\\dp\\accec\\Elementy_gotowe_jp.xlsx"

line_acc = pd.read_csv('line_acc.csv', index_col=0)

def acc_report_to_txt(chosen_path):
    wb = openpyxl.load_workbook(chosen_path)
    sheet = wb['Elementy_gotowe']
    list_of_acc = list()
    all_rows = list(sheet.rows)[7:]


    for row in all_rows:

        if row[2].value is not None and row[2].value != "BLOK":
            pattern_to_length = re.compile(r'(?<=L=)\d+')
            pattern_to_acc = re.compile('liniowy')
            catalog = row[6].value

            if len(pattern_to_acc.findall(row[-2].value)) == 0:

                if (line_acc == catalog).any().any():
                    acc_length = (pattern_to_length.findall(row[3].value))
                    try:
                        acc_length = acc_length[0]

                    except:
                        print(f'Nie wczytano długości dla {row[2].value}, {row[3].value}')
                        acc_length = ''

                    list_of_acc.append((row[2].value, f'{row[5].value}§{row[3].value}§{acc_length}§{row[6].value}§§§§'))
                else:
                    list_of_acc.append((row[2].value, f'{row[5].value}§{row[3].value}§§{row[6].value}§§§§'))

            elif pattern_to_acc.findall(row[-2].value):
                list_of_acc.append((row[2].value, f'{row[5].value}§{row[3].value}§{row[4].value}§{row[6].value}§§§§'))

            else:
                continue

        else:
            continue

    return list_of_acc





if __name__ == '__main__':
    print(acc_report_to_txt(chosen_path))
