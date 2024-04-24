def mass_to_dict(name_of_abs):
    """
    Function to convert mass from abs file to mass sorted by diameters.
    :param name_of_abs:
    :return:
    """
    
    #   import data from abs file
    full_name_of_abs = str(name_of_abs)+'.abs'

#   dictionaries with data abut bars

    mass_final = {
                  'name': name_of_abs,
                  'total': 0,
                  4: 0,
                  5: 0,
                  6: 0,
                  8: 0,
                  10: 0,
                  12: 0,
                  14: 0,
                  16: 0,
                  18: 0,
                  20: 0,
                  22: 0,
                  25: 0,
                  28: 0,
                  32: 0,
                  40: 0,
                  42: 0,
                  45: 0
                  }
    mass_of_bars = {
                  4: 0.22,
                  5: 0.15,
                  6: 0.22,
                  8: 0.39,
                  10: 0.62,
                  12: 0.89,
                  14: 1.21,
                  16: 1.58,
                  18: 2.00,
                  20: 2.46,
                  22: 2.98,
                  25: 3.85,
                  28: 4.83,
                  32: 6.31,
                  40: 9.86,
                  42: 10.87,
                  45: 12.48
                  }     

    with open(full_name_of_abs, 'r') as file:
        #   creation of list with bars
        full_desc = file.readlines()

        #   import attributtes of single bar
        for position in full_desc:

            position_divided = position.split('@')
            length_of_bar = int(position_divided[5].replace(position_divided[5][0], ''))
            quantity_of_bar = int(position_divided[6].replace(position_divided[6][0], ''))
            diameter_of_bar = int(position_divided[8].replace(position_divided[8][0], ''))
            mass_of_meter = mass_of_bars[diameter_of_bar]
            mass_of_bar = mass_of_meter * quantity_of_bar * length_of_bar/1000

            #   addition of single bars to general dictionary
            mass_final[diameter_of_bar] += mass_of_bar 
            mass_final['total'] += mass_of_bar 
    return mass_final
