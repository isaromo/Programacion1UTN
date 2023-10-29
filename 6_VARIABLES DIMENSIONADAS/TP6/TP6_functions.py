import random

def show_array(array):
    print("\n|", end=" ")

    for n in array:
        print(n, end= " | ")

def add_students(school):
    print("--Ingrese los nombres de pila de los alumnos de nivel", school, "\nPara finalizar ingrese 'x'--")

    students = set()
    while True:
        entry = input()
        
        if entry == "x":
            return students

        students.add(entry)

def fill_goals(goals):
    for row in range(0,10):
        goals_row = []
        for col in range(0,10):
            if col == row:      #si fila y columna son iguales se ignora (un equipo no puede jugar contra sí mismo) y se le agrega 0 al array
                goals_row.append(0)
                continue

            goal = int(input(f"GOLES DE E({row+1}) VS. E({col+1}): "))
            goals_row.append(goal)  #genero una lista para cada fila
        goals.append(goals_row)     #le agrego a la lista final las listas por fila
    
    return goals

def show_goals(matrix):
    for row in matrix:
        show_array(row)

def show_outcomes(table):
    for team in table:
        outcome = list(team_outcome(table, table.index(team)))  #le paso a la función la tabla completa y el equipo específico, ya que retornará los resultados por cada equipo
        print(f"\n***EQUIPO {table.index(team) + 1}***")
        print("Triunfos: ", outcome[0])
        print("Derrotas: ", outcome[1])
        print("Empates: ", outcome[2])

        goals_marked = list(marked_received_goals(table, table.index(team)))
        print(">Goles marcados: ", goals_marked[0])
        print(">Goles recibidos: ", goals_marked[1])
        print(">Diferencia de goles: ", abs(goals_marked[0] - goals_marked[1]))

def team_outcome(goals, row):
    wins = 0
    ties = 0
    defeats = 0

    for col in range(0,10):
        if row == col:
            continue    #ignoro la diagonal principial
        
        if goals[row][col] > goals[col][row]:
            wins += 1
        elif goals[row][col] < goals[col][row]:
            defeats += 1
        else:
            ties += 1
    
    return wins, defeats, ties

def marked_received_goals(goals, row):
    #por cada equipo de la tabla...
    marked = 0
    received = 0

    for col in range(0,10):
        marked += goals[row][col]   #sumo los goles hechos por el equipo (los valores de las columnas)
        received += goals[col][row]     #sumo los goles hechos contra el equipo (tomo el valor de la columna y la invierto con la fila para obtener el equipo adverso)

    return marked, received

def fill_cards():
    emojis = ["💚", "💚", "🤍", "🤍", "💛", "💛"]
    cards = [[0,0,0], [0,0,0]]

    for i in range(0,2):
        for j in range(0,3):
            cards[i][j] = random.choice(emojis)    #le doy a la carta un corazón random
            emojis.remove(cards[i][j])  #le borro al array de emojis el corazón asignado recien, para ir achicando las opciones a dar a las otras cartas
    
    return cards

def show_cards(card):
    for i in range(0,2):
        for j in range(0,3):
            print(card[i][j], end=" ")
        print("")
    
    print("")

def turn_cards_around(emojis):
    squares = [["⬜","⬜","⬜"], ["⬜","⬜","⬜"]]
    counter = 0
    both_hearts = []
    
    while counter < 2 :
        card_choice = int(input())

        if card_choice == 1:
            squares[0][0] = emojis[0][0]
            show_cards(squares)
            both_hearts.append([0,0])
        elif card_choice == 2:
            squares[0][1] = emojis[0][1]
            show_cards(squares)
            both_hearts.append([0,1])
        elif card_choice == 3:
            squares[0][2] = emojis[0][2]
            show_cards(squares)
            both_hearts.append([0,2])
        elif card_choice == 4:
            squares[1][0] = emojis[1][0]
            show_cards(squares)
            both_hearts.append([1,0])
        elif card_choice == 5:
            squares[1][1] = emojis[1][1]
            show_cards(squares)
            both_hearts.append([1,1])
        elif card_choice == 6:
            squares[1][2] = emojis[1][2]
            show_cards(squares)
            both_hearts.append([1,2])
        else:
            print("Opción inválida.")
            continue
    
        counter += 1
    
    return both_hearts

def validate_equal_cards(both_hearts, cards):       #corregir indices
    if cards[both_hearts][0] == cards[both_hearts][1]:
        cards[both_hearts][0] = "✅"
        cards[both_hearts][1] = "✅"
    else:
        print("❌¡LAS CARTAS NO SON IGUALES!❌")