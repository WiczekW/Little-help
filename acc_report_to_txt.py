import glob as gb
from is_txt_oneline import is_empty_acc
import os
import openpyxl
import pandas as pd
import re

chosen_path = "C:\\Users\\Wik\\Desktop\\dp\\accec\\Elementy_gotowe_jp.xlsx"
def acc_report_to_txt(chosen_path):
    wb = openpyxl.load_workbook(chosen_path)
    sheet = wb['Elementy_gotowe']
    list_of_acc = list()
    all_rows = list(sheet.rows)[7:]


    for row in all_rows:
        if row[2].value is not None and row[-2].value != 'Element gotowy liniowy':
            pattern = re.compile(r'L=')
            if pattern.findall(row[3].value):
                list_of_acc.append((row[2].value,f'{row[5].value}§{row[3].value}§dluuuugo§{row[6].value}§§§§'))
            else:
                list_of_acc.append((row[2].value,f'{row[5].value}§{row[3].value}§§{row[6].value}§§§§'))
        else:
            continue

    print(list_of_acc)


acc_report_to_txt(chosen_path)