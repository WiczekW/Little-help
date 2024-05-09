import glob as gb
import os.path
import pandas as pd


class Look_for_prj():
    """
    Class to handle looking for path of company server
    """
    def __init__(self):
        """

        """
        self.path_to_prj = str()
        self.path_to_prod_fold = str()
        self.subproduction_folders = str()

    def single_prj(self, shortcut: str) -> list:
        """
        Function to find and sort paths to production folders of project.
        :param shortcut: of a project as a string
        :return: list of paths to production folders
        """
        shortcut = shortcut.upper()
        if shortcut[-1] == 'R':
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

        paths = self.subproduction_folders
        folders_creation_time = []
        for path in paths:
            creation_time = os.path.getctime(path)
            folders_creation_time.append(creation_time)

        series_folders_creation_time = pd.Series(index=folders_creation_time, data=paths)
        series_folders_creation_time.sort_index(inplace=True)
        sorted_paths = series_folders_creation_time.tolist()
        self.subproduction_folders = sorted_paths
        return sorted_paths

    def search_txt(self) -> list:
        """
        Funcion to find paths of all txt files from list of subproduction folders.
        :return: paths to txt files
        """
        paths = self.subproduction_folders
        list_of_txt = []
        for path in paths:
            subproduction_txt = gb.glob(path + '\\*.txt')
            for txt_path in subproduction_txt:
                list_of_txt.append(txt_path)
        return list_of_txt

    def search_txt_selected_folder(self, path: str) -> list:
        """
        Searches for txt files in folder from selected path.
        :param path: path to folder as a string
        :return: list of paths to txt files from selected folder
        """
        self.subproduction_folders = [path]
        paths = self.subproduction_folders
        list_of_txt = []
        for path in paths:
            subproduction_txt = gb.glob(path + '\\*.txt')
            for txt_path in subproduction_txt:
                list_of_txt.append(txt_path)
        return list_of_txt



