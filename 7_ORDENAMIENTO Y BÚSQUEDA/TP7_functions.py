def bubble_sort(array):
    for i in range(0, len(array)-1):  
        for j in range(len(array)-1):  

            if(array[j] > array[j+1]):  
                aux = array[j]  
                array[j] = array[j+1]  
                array[j+1] = aux  

    return array  

def selection_sort(array):
    length = len(array)  
    
    for i in range(length-1):  
        min_index = i  

        for j in range(i+1, length):  
            if array[j] < array[min_index]:  
                min_index = j  
        
        array[i], array[min_index] = array[min_index], array[i]  
    
    return array

def insertion_sort(array):
    if len(array) <= 1:
        return  # si el array tiene 0 o 1 elemento ya fue ordenado, return

    for i in range(1, len(array)):  # se itera el array desde el segundo elemento
        key = array[i]  # guardar el elemento para luego insertarlo en la posición correcta
        j = i-1
        while j >= 0 and key < array[j]:  # todos los elementos más grandes que el elemento se moverán adelante
            array[j+1] = array[j]  # se mueven los elementos a la derecha
            j -= 1
        array[j+1] = key

    return array

def show_array(array):
    for i in array:
        print(i, end=" ")
    print("")