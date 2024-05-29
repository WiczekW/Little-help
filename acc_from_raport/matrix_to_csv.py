import pandas as pd


def import_line_acc(path_to_matrix: str) -> pd.DataFrame:

    matrix_df = pd.read_excel(path_to_matrix, sheet_name="Matryca")
    matrix_df = matrix_df[['Indeks']].where(matrix_df['Jednostka'] == 'm')
    matrix_df.dropna(inplace=True, axis=0)
    matrix_df.to_csv('line_acc.csv', columns=['Indeks'], index_label='ID')
    print(f'Wygenerowano plik line_acc.csv')
    return matrix_df