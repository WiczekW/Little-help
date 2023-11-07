import glob as gb
import os.path
import pandas as pd


class Look_for_prj():
    def __init__(self):


        self.path_to_prj = 'here will be path to single project folder'
        self.path_to_prod_fold = 'here will be path to probuction folder in project'
        self.subproduction_folders = 'here will be list to production folders in production'

    def single_prj(self, shortcut):

        shortcut = shortcut.upper()
        if shortcut[-1] == 'Q':
            self.path_to_single_prj = gb.glob('\\\\dp.pekabex.poznan\\projekty2024\\' + shortcut + '*')
        elif shortcut[-1] == 'P':
            self.path_to_single_prj = gb.glob('\\\\dp.pekabex.poznan\\projekty2023\\' + shortcut + '*')
        elif shortcut[-1] == 'O':
            self.path_to_single_prj = gb.glob('\\\\dp.pekabex.poznan\\projekty2022\\' + shortcut + '*')
        elif shortcut[-1] == 'N':
            self.path_to_single_prj = gb.glob('\\\\dp.pekabex.poznan\\projekty2021\\' + shortcut + '*')
        elif shortcut[-1] == 'M':
            self.path_to_single_prj = gb.glob('\\\\dp.pekabex.poznan\\projekty2020\\' + shortcut + '*')
        elif shortcut[-1] == 'L':
            self.path_to_single_prj = gb.glob('\\\\dp.pekabex.poznan\\projekty2019\\' + shortcut + '*')
        else:
            print('Nie odnaleziono')
        self.path_to_prod_fold = self.path_to_single_prj[0] + '\\Na produkcje\\'
        self.subproduction_folders = gb.glob(self.path_to_prod_fold + '\\*')

        #   sorting subproduction folders by date
        paths = self.subproduction_folders
        folders_creation_time = []
        for path in paths:
            creation_time = os.path.getctime(path)
            folders_creation_time.append(creation_time)

        series_folders_creation_time = pd.Series(index=folders_creation_time, data=paths)
        series_folders_creation_time.sort_index(inplace=True)
        sorted_paths = series_folders_creation_time.tolist()
        self.subproduction_folders = sorted_paths



    def search_txt(self):
        paths = self.subproduction_folders
        list_of_txt = []
        for path in paths:
            subproduction_txt = gb.glob(path + '\\*.txt')
            for txt_path in subproduction_txt:
                list_of_txt.append(txt_path)
        return list_of_txt

    def search_txt_selected_folder(self, path):
        self.subproduction_folders = [path]
        paths = self.subproduction_folders
        list_of_txt = []
        for path in paths:
            subproduction_txt = gb.glob(path + '\\*.txt')
            for txt_path in subproduction_txt:
                list_of_txt.append(txt_path)
        return list_of_txt



