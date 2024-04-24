import tkinter as tk
from tkinter import filedialog
# from PIL import Image, ImageTk
import template_info
from analyze_prj import c2_prj
from analyze_folder import c2_folder
from analyze_foler_extended import c2_folder_extended
from xlsx_n_abs_to_txt_v1 import txt_gen
from acc_uni_to_txt import acc_uni_to_txt
from xnat_v2 import df_integration, row_to_txt

root = tk.Tk()
root.title('LITTLE HELP v0.42')

def command_folder():
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    c2_folder(path)


def command_folder_extended():
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    c2_folder_extended(path)


def command_txt_generate():
    path = filedialog.askopenfile(parent=root, mode='r', title='Wybierz plik')
    txt_gen(path.name)

def command_acc_uni_to_txt():
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    acc_uni_to_txt(path)

def command_txt_generate_v2():
    path = filedialog.askdirectory(parent=root, title='Wybierz folder')
    row_to_txt(df_integration(path), path)

def show_info():
    popup = tk.Toplevel(root)
    popup.title('Info')
    label = tk.Label(popup, text=template_info.info_text, justify='left')
    label.pack()
    #image = Image.open('dim.png')
    #image_tk=ImageTk.PhotoImage(image)
    #image_label = tk.Label(popup, image=image_tk)
    #image_label.image = image_tk
    #image_label.pack()
    #   text
    signature = tk.Label(popup, text='Małe pomoce - Wiktor Gajewski 2023', height=1, width=40)
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

btn5 = tk.Button(c, text='Dodaj akc do TXT', width=button_w,
             height=button_h, command=command_acc_uni_to_txt)
btn5.grid(column=3, row=2)

btn6 = tk.Button(c, text='INFO', width=button_w,
             height=button_h, command=show_info)
btn6.grid(column=4, row=3)

btn7 = tk.Button(c, text='ZAMKNIJ', width=button_w,
             height=button_h, command=root.destroy)
btn7.grid(column=4, row=4)

btn7 = tk.Button(c, text='Generuj TXT v2', width=button_w,
             height=button_h, command=command_txt_generate_v2)
btn7.grid(column=2, row=3)


root.mainloop()