import tkinter as tk
from tkinter import filedialog
import template_info
from analyze_prj import c2_prj
from analyze_folder import c2_folder
from analyze_foler_extended import c2_folder_extended
from xlsx_n_abs_to_txt_v1 import txt_gen
from acc_uni_to_txt import acc_uni_to_txt
from xnat_v2 import df_integration, row_to_txt
from acc_from_raport.matrix_to_csv import import_line_acc
from acc_from_raport.acc_raport import acc_raport_to_list
from acc_from_raport.write_acc_to_txt import TxtWriter


root = tk.Tk()
root.title('LITTLE HELP v0.45')



def command_folder():
    """
    Button function to choose folder and initialize c2_folder function.
    """
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    c2_folder(path)


def command_folder_extended():
    """
    Button function to choose folder and initialize c2_folder_extended function.
    """
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    c2_folder_extended(path)


def command_txt_generate():
    """
    Button function to choose file and initialize generation of txt files.
    """
    path = filedialog.askopenfile(parent=root, mode='r', title='Wybierz plik')
    txt_gen(path.name)


def command_acc_uni_to_txt():
    """
    Button function to choose folder and initialize addition of accessories to txt from uni files.
    """
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    acc_uni_to_txt(path)


def command_txt_generate_v2():
    """
    Button function to choose file and initialize generation of txt files.
    """
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    row_to_txt(df_integration(path), path)


def execute_import_line_acc():
    """
    Button function to choose file and import line accessories as csv
    """
    path = filedialog.askopenfile(parent=root, mode='r', title='Wybierz plik')
    import_line_acc(path.name)


def add_acc_raport_to_txt():
    """
    Button function to choose file and add accessories from excel to txt files
    """
    path = filedialog.askopenfile(parent=root, mode='r', title='Wybierz plik')
    list_of_acc = acc_raport_to_list(path.name)
    if list_of_acc is False:
        return False
    txt_write = TxtWriter(list_of_acc, path.name)
    txt_write.search_for_elements()
    txt_write.write_to_txt()




def show_info():
    """
    Button function to view documentation
    """
    popup = tk.Toplevel(root)
    popup.title('Info')

    label = tk.Label(popup, text=template_info.info_text, justify='left')
    label.pack()

    #   text
    signature = tk.Label(popup, text='Małe pomoce - Wiktor Gajewski 2024', height=1, width=40)
    signature.pack()
    close_btn = tk.Button(popup, text='Zamknij', command=popup.destroy)
    close_btn.pack()


canvas_w = 300
canvas_h = 300
button_w = 20
button_h = 1
info1 = 'ANALIZUJ TXT'
info2 = 'ALLPLAN'
info3 = 'PLANBAR'
info4 = ''
c = tk.Canvas(root, width=canvas_w, height=canvas_h, )
c.grid(columnspan=4, rowspan=4)
c.pack()

inf_1 = tk.Label(c, text=info1)
inf_1.grid(column=1, row=1)

inf_2 = tk.Label(c, text=info2)
inf_2.grid(column=2, row=1)

inf_3 = tk.Label(c, text=info3)
inf_3.grid(column=3, row=1)

inf_4 = tk.Label(c, text=info4)
inf_4.grid(column=4, row=1)

btn1 = tk.Button(c, text='TXT z katalogu', width=button_w,
             height=button_h, command=command_folder_extended)
btn1.grid(column=1, row=2)

btn2 = tk.Button(c, text='C2 z katalogu', width=button_w,
             height=button_h, command=command_folder)
btn2.grid(column=1, row=3)

btn3 = tk.Button(c, text='C2 z tematu', width=button_w,
             height=button_h, command=c2_prj)
btn3.grid(column=1, row=4)

btn4 = tk.Button(c, text='Generuj TXT v1', width=button_w,
             height=button_h, command=command_txt_generate)
btn4.grid(column=2, row=2)

btn5 = tk.Button(c, text='Dodaj akcesoria - uni', width=button_w,
             height=button_h, command=command_acc_uni_to_txt)
btn5.grid(column=3, row=2)

btn6 = tk.Button(c, text='Info', width=button_w,
             height=button_h, command=show_info)
btn6.grid(column=4, row=3)

btn7 = tk.Button(c, text='Zamknij', width=button_w,
             height=button_h, command=root.destroy)
btn7.grid(column=4, row=4)

btn7 = tk.Button(c, text='Generuj TXT v2', width=button_w,
             height=button_h, command=command_txt_generate_v2)
btn7.grid(column=2, row=3)

btn8 = tk.Button(c, text='Dodaj akcesoria - excel', width=button_w,
             height=button_h, command=add_acc_raport_to_txt)
btn8.grid(column=2, row=4)

btn9 = tk.Button(c, text='Zaimportuj matrycę', width=button_w,
             height=button_h, command=execute_import_line_acc)
btn9.grid(column=4, row=2)


root.mainloop()
