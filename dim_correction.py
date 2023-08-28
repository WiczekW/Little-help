#funkcja ustawiająca wymiary we właściwych miejscach txt

#dla ściany pełnej długość jest największa, szerokość najmniejsza, wysokość pośrednia

def dim_correction(element):

    dim1 = element[37]
    dim2 = element[39]
    dim3 = element[41]

    dim_list = [dim1, dim2, dim3]
    dim_list.sort()

    elem_length = dim_list[2]
    elem_width = dim_list[0]
    elem_hight = dim_list[1]
    
    
    return elem_length, elem_width, elem_hight


    
