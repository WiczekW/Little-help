import openpyxl
import pandas as pd
import re


def acc_report_to_txt(chosen_path: str) -> list|bool:
    """
    Function to convert excel raport and imported csv file to list of tuples. Function runs through the sheet
    and convert it to a tuple. Line accessories are handled in two ways: the first one is looking for the "=digit"
    patter in name, it's triggered by Index number compared to csv file. The second way finds 'liniowy' patter in
    type of accessories and then divide length from sheet by quantity - avg length is stored in tuple.
    :param chosen_path: path to excel raport
    :return: list of tuples with attributes of accessories in precast elements
    """
    wb = openpyxl.load_workbook(chosen_path)
    sheet = wb['Elementy_gotowe']
    list_of_acc = list()
    all_rows = list(sheet.rows)[7:]

    try:
        line_acc = pd.read_csv('line_acc.csv', index_col=0)
    except FileNotFoundError:
        print(f'Nie odnaleziono pliku line_acc.csv')
        return False

    for row in all_rows:

        if row[2].value is not None and row[2].value != "BLOK":
            pattern_to_length = re.compile(r'(?<==)\d+')
            pattern_to_acc = re.compile('liniowy')
            catalog = row[6].value

            if len(pattern_to_acc.findall(row[-2].value)) == 0:

                if (line_acc == catalog).any().any():
                    acc_length = (pattern_to_length.findall(row[3].value))
                    try:
                        acc_length = acc_length[0]
                    except IndexError:
                        print(f'Nie wczytano długości dla {row[2].value}, {row[3].value}')
                        acc_length = ''

                    list_of_acc.append((row[2].value, f'{row[5].value}§{row[3].value}§{acc_length}§{row[6].value}§§§§'))
                else:
                    list_of_acc.append((row[2].value, f'{row[5].value}§{row[3].value}§§{row[6].value}§§§§'))

            elif pattern_to_acc.findall(row[-2].value):

                try:
                    avg_length = float(row[4].value) / float(row[5].value)
                    avg_length = round(avg_length)
                    list_of_acc.append((row[2].value, f'{row[5].value}§{row[3].value}§{avg_length}§{row[6].value}§§§§'))
                except TypeError:
                    print(f'Nie wczytano długości dla {row[2].value}, {row[3].value}')

            else:
                continue

        else:
            continue

    return list_of_acc


if __name__ == '__main__':
    chosen_path = "C:\\Users\\Wik\\Desktop\\dp\\accec\\Elementy_gotowe_jp.xlsx"
    print(acc_report_to_txt(chosen_path))

