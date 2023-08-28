import tkinter as tk
from tkinter import filedialog
from analyze_prj import c2_prj
from analyze_folder import c2_folder
from analyze_foler_extended import c2_folder_extended
from xlsx_n_abs_to_txt_v1 import txt_gen


root = tk.Tk()
root.title('LITTLE HELP')


def command_folder():
    path = filedialog.askdirectory(parent=root)
    c2_folder(path)


def command_folder_extended():
    path = filedialog.askdirectory(parent=root)
    c2_folder_extended(path)


def command_txt_generate():
    path = filedialog.askopenfile(parent=root, mode='r', title='Choose a file')
    txt_gen(path.name)


instructions1 = tk.Label(root, text='''GENERACJA TXT
w tym samym folderze muszą się znaleźć:
 - excel - txt_allplan_v17_S_czysty
 - pliki abs''', justify='center')

instructions1.pack()

btn_generate_txt = tk.Button(root, text='Wybierz plik excel', command=command_txt_generate)
btn_generate_txt.pack()

instructions2 = tk.Label(root, text='''ANALIZA TXT
generacja pliku excel z danymi''', justify='center')

instructions2.pack()

btn_analyze_prj = tk.Button(root, text='Generuj C2 dla tematu', command=c2_prj)
btn_analyze_prj.pack()

btn_analyze_folder = tk.Button(root, text='Generuj C2 dla katalogu', command=command_folder)
btn_analyze_folder.pack()

btn_analyze_folder = tk.Button(root, text='Analizuj txt z katalogu', command=command_folder_extended)
btn_analyze_folder.pack()

btn_exit = tk.Button(root, text='Zamknij', command=root.quit)
btn_exit.pack()

#   text
signature = tk.Label(root, text='Małe pomoce - Wiktor Gajewski 2023', height=1, width=40)
signature.pack()


root.mainloop()
