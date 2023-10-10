
def is_txt_oneline(path):
    with open(path, 'r') as file:
        condition = len(file.readlines())
        if condition > 1:
            return False
        else:
            return True

