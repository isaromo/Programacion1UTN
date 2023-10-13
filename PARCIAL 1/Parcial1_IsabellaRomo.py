high_even = 0
odd_sum = 0
odd_counter = 0
vocal_A = 0
vocal_E = 0
vocal_I = 0
vocal_O = 0
vocal_U = 0

name = input("Ingrese su nombre: ")
print("¡ Hola ", name, "!")
print("-------MENÚ-------")
print("1. Juego de números")
print("2. Juego de palabras")
print("------------------")
game = int(input())

if game == 1:
    print(name, ", vas a jugar al JUEGO DE NÚMEROS")

    print("Ingresa números enteros. Para salir ingresa 0")

    while True:     #while True para que el usuario pueda seguir ingresando numeros hasta que ingrese 0
        number = int(input())
        if number % 2 != 0: #si el número ingresado es impar...
            odd_sum += number
            odd_counter += 1
        else:   #si el número ingresado es par...
            if number > high_even:
                high_even = number

        if number == 0:
            break
    
    print("MAYOR NÚMERO PAR: ", high_even)
    print("PROMEDIO IMPARES: ", odd_sum/odd_counter)

elif game == 2:
    print(name, ", vas a jugar al JUEGO DE PALABRAS")
    print("Ingresa una frase cualquiera")
    phrase = input().upper()

    for i in phrase:    #se recorre cada carácter en la frase
        if i == "A":
            vocal_A += 1
        elif i == "E":
            vocal_E += 1
        elif i == "I":
            vocal_I += 1
        elif i == "O":
            vocal_O += 1
        elif i == "U":
            vocal_U += 1
    
    print(name, ", en tu frase hay:\n", vocal_A, " 'A'\n", vocal_E, " 'E'\n", vocal_I, " 'I'\n", vocal_O, " 'O'\n", vocal_U, " 'U'")
    
elif game > 2:
    print("Esa opción es incorrecta!")