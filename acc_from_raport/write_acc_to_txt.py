import os
import re


def is_txt_oneline(path):
    """
    Checks if the txt file is one line of text.
    :param path: path to txt file as a string
    :return: bool
    """
    with open(path, 'r') as file:
        condition = len(file.readlines())
        if condition > 1:
            return False
        else:
            return True


class TxtWriter:

    def __init__(self, list_of_acc: list, path_to_raport: str):
        self.list_of_acc = list_of_acc
        self.list_of_elements = list()
        self.path_to_raport = path_to_raport
        self.path_to_dir = os.path.dirname(path_to_raport)

    def search_for_elements(self):
        """
        Funcion to search for all elements names in the list of accessories initialized in self.list_of_acc
        :return: list of names
        """

        for i in self.list_of_acc:
            if i[0] not in self.list_of_elements:
                self.list_of_elements.append(i[0])
            else:
                continue

        return self.list_of_elements

    def write_to_txt(self):
        """
        Function to write all accessories to txt files named in self.list_of_elements
        :return:
        """
        for element in self.list_of_elements:
            path_to_txt = self.path_to_dir + '\\\\' + element + '.txt'

            try:
                if is_txt_oneline(path_to_txt):
                    pass
                else:
                    print(f'Pominięto txt dla {element}. Plik ma więcej niż jedną linię.')
                    continue
            except FileNotFoundError:
                print(f'Nie odnaleziono pliku txt dla elementu {element}')
                continue

            with open(path_to_txt, 'a+', encoding='ANSI') as file:
                file.write('\n')

                for acc in self.list_of_acc:
                    if acc[0] == element:
                        try:
                            file.write(acc[1])
                            file.write('\n')
                        except UnicodeEncodeError:
                            print(f'Nie dodano. Błędny symbol w {acc}')
                    else:
                        continue
                print(f'Dodano akcesoria do elementu {element}')

if __name__ == '__main__':
    pass

