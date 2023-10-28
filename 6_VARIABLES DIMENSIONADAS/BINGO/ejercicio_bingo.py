#BINGO
while True:
    from functions import complete_row, show_card, random_value, ramdom_in_card, bingo_row, bingo_column, bingo_principal_diagonal, bingo_secundary_diagonal

    print("🎊 JUEGO DE BINGO 🎊")

    card=[[0,0,0,0,0]]*5    #se crea el cartón de 5x5
    counter = 0

    #LLENAR CARTÓN
    while counter < 5:
        row = []
        print("---------------------------------------")
        print("Ingrese los valores de la fila ", counter+1)
        card[counter] = complete_row(row, card)     #una vez develta la fila llenada por el usuario se inserta en el carton en la posición de fila correspondiente (card[counter])
        counter+=1

    #MOSTRAR CARTÓN LLENADO POR EL USUARIO
    print("❗ SU CARTÓN DE BINGO ES EL SIGUIENTE: ")
    show_card(card)

    #NÚMEROS DE RULETA Y VERIFICACIONES PARA VER SI EL USUARIO GANÓ
    while True:
        random = random_value()
        print("🎱 EL NÚMERO DE RULETA ES: ", random)

        if ramdom_in_card(random, card):    #random_in_card valida que el numero se encuentre en el cartón, y si lo está lo reemplaza por un 0
            print(f"{random} ENCONTRADO! 😁")
        else:
            print(f"{random} NO ENCONTRADO 😞")
            
        #si cualquiera de las funciones con las cual se gana devuelve True se gana el juego
        if bingo_row(card) or bingo_column(card) or bingo_principal_diagonal(card) or bingo_secundary_diagonal(card):
            print("-----------------------------")
            print("🎉🎉🎉 ¡¡GANASTE!! 🎉🎉🎉")
            show_card(card)
            break

    print("🎲 ¿DESEA JUGAR DE NUEVO? S/N 🎲")
    play_again = input().upper()

    if play_again == "N":
        print("ADIOS")
        break