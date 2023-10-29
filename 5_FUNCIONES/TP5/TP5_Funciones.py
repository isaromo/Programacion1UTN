import functionsTP5

'''#EJERCICIO 1
dni = int(input("Ingrese su DNI: "))
outcome = functionsTP5.valid_dni(dni)
print(f"¿El DNI es válido? {outcome}")


#EJERCICIO 2
phrase = input("Ingrese una frase: ").strip()   #metodo strip para eliminar cualquier espacio que la frase pueda tener al principio y/o al final
print(f"La longitud de la última palabra en la frase '{phrase.upper()}' es de: {functionsTP5.last_word_length(phrase)} carac.")


#EJERCICIO 3
counter = 1
while True:
    print("Ingrese el SOCIO Nº", counter)
    counter += 1
    name = input("***Para salir ingrese ENTER***\nNombre en formato [Nombre (Nombre2) Apellido]: ").strip()
    if name == "":  #si el nombre esta vacío se termina el programa
        break

    dni = int(input("DNI: "))

    while (functionsTP5.valid_dni(dni) == False):   #mientras el DNI no sea válido, se le vuelve a pedir al usuario
        dni = int(input("DNI: "))

    print(f"ID -> ", name[0:name.find(' ')], functionsTP5.last_word_length(name), str(dni)[0:3], sep = "")  #ID-> (primer nombre) (longitud del apellido) (primeros 3 dig del DNI), y agrego el sep="" para que no haya separación entre las variables
    print("")

    
#EJERCICIO 4
num1 = int(input("Número entero 1: "))
num2 = int(input("Número entero 2: "))
print(f"¿Es {num1} múltiplo de {num2}? {functionsTP5.multiple_or_not(num1,num2)}")


#EJERCICIO 5
amount_days = int(input("Cantidad de días que va a ingresar: "))

for i in range(1, amount_days+1):
    print("DÍA ", i)
    max_t = float(input("Temperatura máxima: "))
    min_t = float(input("Temperatura mínima: "))

    print("TEMPERATURA MEDIA: ", functionsTP5.average_temperature(max_t, min_t))

    
#EJERCICIO 6
phrase = input("Ingrese una frase: ")
print(functionsTP5.separate_words(phrase))


#EJERCICIO 7
numbers = []
print("Ingrese números. Para salir presione ENTER")

while True:
    num = input()   #tomo num como string para poder hacer la verificación en el if, ya que no se le puede asignar un vacío a un int
    if num == "":
        break
    else:
        numbers.append(int(num))    #si no es un vacío, lo parseo y se lo agrego a la lista

functionsTP5.highest_lowest(numbers)


#EJERCICIO 8
radius = float(input("Ingrese el radio del círculo: "))
functionsTP5.area_perimeter(radius)


#EJERCICIO 9
tries = 3
while tries > 0:
    user = input("Usuario > ")
    password = input("Contraseña > ")

    if (functionsTP5.login(user, password) == True):
        print("Accedido")
        break
    else:
        print("Usuario o contraseña incorrecta.")
        tries -= 1

        
#EJERCICIO 10
counter = 0
shopping_cart = {}
print("Ingrese los productos y sus descuentos. Para salir ingrese 0 al momento de ingresar el precio")

while True:
    counter += 1
    print("PRODUCTO ", counter)
    price = float(input("Precio: "))

    if price == 0:
        break

    disc = float(input("Descuento: "))
    shopping_cart[price] = disc     #agrego el par al diccionario

print("Precio final: $", functionsTP5.discounts(shopping_cart))


#EJERCICIO 11
radiuses = []
print("Ingrese 5 radios de círculos distintos:")
for i in range(0,5):
    radiuses.append(int(input()))

print("ÁREAS:")
returned_list = functionsTP5.ejercicio11(functionsTP5.area_circle, radiuses)

for i in returned_list:
    print(i, end= " | ")


#EJERCICIO 12
phrase = input("Ingrese una frase: ")
print(functionsTP5.phrase_to_dictionary(phrase))


#EJERCICIO 13
array = [2,5,8]
print("El módulo del vector...")
for i in array:
    print(i, end= "  ")
print("\n... es ", functionsTP5.module(array))


#EJERCICIO 14
number = int(input("Ingrese un número: "))
print(f"Es {number} primo? {functionsTP5.prime_or_not(number)}")


#EJERCICIO 15
print("Ingrese números. Para salir ingrese ENTER")
num_array = []

while True:
    number = input()
    if number == "":
        break
    else:
        num_array.append(int(number))

print(functionsTP5.all_factorials(num_array))


#EJERCICIO 16
num = int(input("Ingrese un número: "))
dig = int(input("Ingrese un dígito: "))
functionsTP5.digit_in_num(num, dig)


#EJERCICIO 17
print("Ingrese números primos. Se detendrá el programa cuando el número NO sea primo")
numbers_array = []
highest = 0
while True:     #while True para ingresar números primos y agregarlos a un array
    number = int(input)
    if functionsTP5.prime_or_not(number) == False:      #si el número no es primo se rompe el ciclo
        break
    
    numbers_array.append(number)

    if number > highest:
        highest = number

for n in numbers_array:     #por cada número primo...  
    print(f"---- {n} ----")
    print("SUMA DE DÍGITOS: ", functionsTP5.sum_digits(n))  #muestro su suma de dígitos
    dig = int(input("Dígito a encontrar: "))    #pido un dígito a encontrar y ejecuto la función correspondiente
    functionsTP5.digit_in_num(n, dig)
    print(f"FACTORIAL DEL MAYOR:\n !{n} = ")    #muestro el factorial del mayor primo ingresado
    print(functionsTP5.factorial(n))'''