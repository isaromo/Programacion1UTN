#Llenar Filas
import random

def complete_row(row, card): 
    counter = 0

    while counter < 5:
        print("Ingrese un numero único (de 1 a 75) para completar su cartón")
        value_entered = int(input())

        if valid_value(value_entered, card, row): #se ejecuta la funcion que corrobora que el numero ingresado sea valido
                row.append(value_entered) #si lo es se inserta en la fila temporal 
                counter+=1
        else:
            print("Ese número es inválido")

    return row

def valid_value(value, card, row):
    if value < 1 or value > 75:
            print("El valor debe estar entre 1 y 75")
            return False
    elif value in row: #comprobamos que en la fila temporal no se haya ingresado el valor
        return False
    else:
        find_value = False
        for rows in card: #se busca el valor en todo el carton, si se encuentra retorna False
            if value in rows:
                find_value = True
        if find_value:
            return False
        else:
            return True


def show_card(card):    #se recorre el carton y se muestra de forma atractiva
    
    for rows in card:
        for element in rows:
            if element < 10:
                print("{0}{1} | ".format(0, element), end="")
            else:
                print(element, end= " | ")
        print("\n------------------------")

def random_value(): 
    bingo_values=[]     #creamos una lista en donde ir agregando los números de ruleta para que sean sacados solo una vez y no se repitan
    value = random.randint(1, 76)   #genera un valor aleatorio entre 1 y 76
    
    while value in bingo_values: 
        value = random.randint(1, 76)   #si el valor ya fue sacado, se vuelve a sacar otro número
    
    bingo_values.append(value)
    return value

def ramdom_in_card(value, card):

    for rows in card:
        for i in range(0, 5):
            if rows[i] == value:    #verifica si el valor random generado se encuentra en el carton
                rows[i] = 0     #si se encuentra en el carton se reemplaza por 0
                return True
    return False

def bingo_row(card):
    counter = 0
    
    for row in card:
        for j in row:
            if j == 0:
                counter += 1    #por cada valor igual a 0 que se encuentra en una fila, se incrementa el contador en 1

        if counter == 5:    #si el contador llega a 5 es porque la fila tiene todos '0'
            print("FILA ", (card.index(row))+1, " COMPLETADA")
            return True
        else:
            counter = 0     #si el contador no llega a 5, entonces se reinicia para verificar la siguiente fila

    return False

def bingo_column(card):
    counter = 0

    for i in range(0,5):
        for row in card:
            if row[i] == 0:
                counter +=1     #por cada valor igual a 0 que se encuentra en una columna, se incrementa el contador en 1

        if counter == 5:    #si el contador llega a 5 es porque la columna tiene todos '0'
            print("COLUMNA ", i+1, " COMPLETADA")
            return True
        else:
            counter = 0     #si el contador no llega a 5, entonces se reinicia para verificar la siguiente columna
    return False

def bingo_principal_diagonal(card):
    counter = 0

    for i in range(0,5):
        if card[i][i] == 0:     #para la diag princ, la posición de la fila y la columna deben ser la misma, por lo tanto "[i][i]"
            counter += 1    #si se encuentra un '0' en la diagonal principal, se incrementa el contador

    if counter == 5:    #si el contador llega a 5 es porque la columna tiene todos '0'
        print("DIAGONAL PRINCIPAL COMPLETADA")
        return True
    else:
        return False

def bingo_secundary_diagonal(card):
    counter = 0
    i = 4

    for row in range(0,5):
        if card[row][i] == 0:   #para recorrer la diag sec, la fila se va incrementando mientras i se va decrementando
            counter+=1  #si se encuentra un '0' en la diagonal secundaria, se incrementa el contador
        i-=1  
    
    if counter == 5:    #si el contador llega a 5 es porque la columna tiene todos '0'
        print("DIAGONAL SECUNDARIA COMPLETADA")
        return True
    else:
        return False