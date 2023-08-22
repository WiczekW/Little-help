import tkinter as tk
from tkinter import filedialog
from analyze_prj import c2_prj
from analyze_folder import c2_folder
from analyze_foler_extended import c2_folder_extended
root = tk.Tk()
root.title('TXT TO EXCEL')

def command_folder():
    path = filedialog.askdirectory(parent=root)
    c2_folder(path)

def command_folder_extended():
    path = filedialog.askdirectory(parent=root)
    c2_folder_extended(path)


btn_analyze_prj = tk.Button(root, text='Generuj C2 dla tematu', command=c2_prj)
btn_analyze_prj.pack()

btn_analyze_folder = tk.Button(root, text='Generuj C2 dla katalogu', command=command_folder)
btn_analyze_folder.pack()

btn_analyze_folder = tk.Button(root, text='Analizuj txt dla katalogu', command=command_folder_extended)
btn_analyze_folder.pack()

btn_exit = tk.Button(root, text='Zamknij', command=root.quit)
btn_exit.pack()

#text
signature = tk.Label(root,text='Małe pomoce - Wiktor Gajewski 2023', height=1, width=30)
signature.pack()


root.mainloop()