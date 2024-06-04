
info_text = '''
ANALIZUJ TXT
Analizuje pliki txt ze wskazanego katalogu i zestawia
je w excelu o nazwie "Data_from_txt - CUSTOM" zlokalizowanego 
w folderze programu. 

C2 Z KATALOGU
Analizuje pliki txt ze wskazanego katalogu i zestawia
je w excelu o nazwie "C2_filler - custom" zlokalizowanego 
w folderze programu.  

C2 Z TEMATU
Analizuje pliki txt ze wskazanego projektu i zestawia
je w excelu o nazwie "C2_filler - XXXX". Analizowane są
wszystkie pliki z folderu "Na produkcje". Plik powstaje w
folderze programu. 

DODAJ AKCESORIA - UNI
Funkcja szukająca pików .UNI, na ich podstawie znajduje 
odpowiadające im pliki txt, do których dodaje akcesoria 
oraz kratownice znajdujące się w plikach unitechnik. Pliki txt
muszą zawierać tylko jedną linię tekstu. 

GENERUJ TXT V1
Funkcja generująca pliki txt na podstawie tabeli excela 
generowanej z Allplana raportem txt_allplan_v17_S_czysty.
Stal do plików txt jest dodawana poprzez odnajdywanie plików
abs wg nazw elementów z tabeli. Pliki abs muszą być w tym samym
folderze co wybrany excel. Uwaga! Jeśli w plikach abs nie będzie
siatek zbrojeniowych, nie zostaną one uwzględnione w ogólnej
masie stali. 

GENERUJ TXT V2
Funkcja generująca pliki txt na podstawie dwóch tabel z excela.
Po wskazaniu folderu, funkcja szuka plików o nazwach txt_att_v1 
i txt_zbr_v2 (nazwa spójna z raportami w Allplanie). 
x-długość, y-szerokość, z-wysokość

DODAJ AKCESORIA - EXCEL
Przed pierwszym użyciem należy zaimportować matrycę indeksów 
z dysku. W tym samym folderze co wybrany raport muszą znajdować
się pliki txt z nazwami elementów spójnymi z raportem. 
Funkcja korzysta z raportu "Allplan_elementy_gotowe",
po wciśnięciu przycisku należy go wybrać. 
'''