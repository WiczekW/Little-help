
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


def is_empty_acc(path: str) -> bool:
    """
    Function to check if analyzed txt file includes accessories
    :param path: path to txt file as a string
    :return: bool
    """
    with open(path, 'r') as file:
        analyzed_file = file.readlines()
        if len(analyzed_file) >= 1:
            preCondition_list = list()
            for i in analyzed_file[1:]:
                preCondition_list.append(i.find('§KT'))
            if -1 in preCondition_list:
                return False
        else:
            return True


def is_empty_gird(path: str) -> bool:
    """
    Function to check to analyze if txt file includes girders, by checking existance of lines starting with §KT.
    :param path: path to txt file as a string
    :return: bool
    """
    with open(path, 'r') as file:
        analyzed_file = file.readlines()
        if len(analyzed_file) >= 1:
            preCondition_list = list()
            for i in analyzed_file[1:]:
                preCondition_list.append(i.find('§KT'))
            if 1 in preCondition_list:
                return False
            else:
                return True
        else:
            return True
