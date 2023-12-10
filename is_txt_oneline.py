
def is_txt_oneline(path):
    with open(path, 'r') as file:
        condition = len(file.readlines())
        if condition > 1:
            return False
        else:
            return True



def is_empty_acc(path):
    with open(path, 'r') as file:
        analyzed_file = file.readlines()
        condition = [0, 0]

        # check if there are acc or girders in txt
        if len(analyzed_file) >= 1:
            preCondition_list = list()
            for i in analyzed_file[1:]:
                preCondition_list.append(i.find('§KT'))
            if -1 in preCondition_list:
                return False
        else:
            return True


def is_empty_gird(path):
    with open(path, 'r') as file:
        analyzed_file = file.readlines()
        condition = [0, 0]

        # check if there are acc or girders in txt
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



