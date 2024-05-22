from acc_report_to_txt import acc_report_to_txt
from Production_analyzer.is_txt_oneline import is_txt_oneline

class TxtWriter:

    def __init__(self, list_of_acc):
        self.list_of_acc = list_of_acc

    def search_for_elements(self):
        list_of_elements = list()
        for i in self.list_of_acc:
            if i[0] not in list_of_elements:
                list_of_elements.append(i[0])
            else:
                continue
        print(list_of_elements)

    def search_for_txt(self):
        pass


if __name__ == '__main__':
    from_raport = [('B_04', '1§RURA KARBOWANA FI60/67 L=330mm§§§§§§'),
                   ('B_04', '1§RURA KARBOWANA FI60/67 L=390mm§§§§§§'),
                   ('B_04', '1§RURA KARBOWANA FI60/67 L=390mm§§§§§§'),
                   ('B_04', '1§TALERZYK M16 - ZNAK MONTAŻOWY§§§§§§'),
                   ('B_04', '2§ZAW 4-1x12.5 H=550mm§§§§§§'),
                   ('I_02', '3§PROFIL STALOWY PROSTOKĄTNY 100X50X3 S235JR L=1400mm§§§§§§'),
                   ('I_02', '1§PROFIL STALOWY PROSTOKĄTNY 100X50X3 S235JR L=1400mm§§§§§§'),
                   ('I_02', '1§TALERZYK M16 - ZNAK MONTAŻOWY§§§§§§'),
                   ('I_02', '1§ZAW 32-5X15.2 H=1650mm§§§§§§'),
                   ('I_02', '1§ZAW 32-5X15.2 H=1650mm§§§§§§'),
                   ('I_02', '8§Rura PVC 20x1,1§1500§§§§§'),
                   ('C_18', '2§KOTWA KULOWA (S) 10,0/340 HDG§§SB1708000256§§§§'),
                   ('C_18', '2§PKX_CS_M24 L=300MM§§SB1008004775§§§§'),
                   ('C_18', '2§PRĘT GWINTOWANY M24 DIN976 KL.8.8 GV L=400mm§§§§§§'),
                   ('C_18', '1§RURA KARBOWANA FI60/67 L=330mm§§§§§§'),
                   ('C_18', '1§RURA KARBOWANA FI80/87 L=2000(1890+110)mm§2000§SB2906000038§§§§'),
                   ('C_18', '3§RURA KARBOWANA FI80/87 l=1650§1650§SB2906000038§§§§'),
                   ('C_18', '2§RURA KARBOWANA FI80/87 l=1650§1650§SB2906000038§§§§'),
                   ('C_18', '1§Rura PVC Ø100x1,5 L=400mm§400§SB2906000005§§§§'),
                   ('C_18', '1§SZYNA HMPR-CE-38/17X150 FV L=150§§SB3208001381§§§§'),
                   ('C_18', '1§SZYNA HMPR-CE-38/17X150 FV L=150§§SB3208001381§§§§'),
                   ('C_18', '5§Peszel  Ø40§469§§§§§')]
    x = TxtWriter(from_raport)
    x.search_for_elements()
