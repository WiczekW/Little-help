def convert_symbols(chosen_path):
    input_file = chosen_path
    decrypted_file = chosen_path
    decrypted_file = decrypted_file.replace('.uni', '_dec.uni')

    with open(input_file, encoding='ansi') as file:
        utf_text = file.read()
        ansi_text = utf_text.encode('cp1252', 'ignore').decode('cp1252')


    with open(decrypted_file,'w', encoding='cp1252') as output:
        output.write(ansi_text)




