print("EJERCICIO 1") #ej en inglés
x = 0
while x < 30:
    x += 1
    if x == 15:
        print("Se rompió la ejecución del bucle cuando x valía: ", x)
        break;
    elif x == 4 or x == 6 or x == 10:
        print("Se saltó el valor ", x, " de x")
    else:
        print(x)

print("EJERCICIO 2")
money = 0
print("DEPÓSITO: D + monto a depositar \nRETIRO: R + monto a retirar\n**Para salir apretar Enter**")
while True:
    movement = input().upper()
    d_or_r = movement[0:1]      #separo la letra de los números
    if d_or_r == "D":       #si la letra es D, se deposita (suma)
        money += int(movement[1::])
    elif d_or_r == "R":     #si la letra es R, se retira (resta)
        money -= int(movement[1::])
    elif d_or_r == "":      #si la letra es un vacío, se termina la ejecución
        print("$", money)
        break
    else:           #si la letra es distinta de D o R, se omite
        print("**Comando inválido**")

print("EJERCICIO 3")
primes = 0
print("Ingrese números mayores a 1. Para salir ingrese 0")
while True:
    div_counter = 0
    number = int(input())
    if number < 0:  #valido que el num sea mayor a 1
        print("Número inválido. Ingrese de nuevo")
    if number == 0:     #si el num es 0, rompo la ejecución
        break
    else:   #el num es mayor a 1
        for i in range(1,number+1):     #recorro del 1 hasta el num ingresado,
            if number % i == 0:         #aumento el contador por cada vez que num es divisible
                div_counter += 1
        
        if div_counter == 2:         #si el contador es igual a 2, el num es primo
            primes += 1             #entonces aumento el contador de nums primos

print("Cantidad total de nums primos ingresados: ", primes)

print("EJERCICIO 4")
year1 = int(input("Ingrese el primer año: "))
year2 = int(input("Ingrese el segundo año: "))
for i in range(year1, year2+1):
    if ((i % 4 == 0) and (i % 100 != 0 or i % 400 == 0)) and (i%10 == 0):
        print(i)

print("EJERCICIO 5")
for i in range(1,20):
    if i%2 != 0:
        continue
    else:
        print(i)

print("EJERCICIO 6")
list = [1,4,8,14,54,25,40,98]
found = False
for i in list:  #muestro la lista
    print(i, end=" | ")

num = int(input("\nNúmero a buscar: "))
for i in list:
    if i == num:
        found = True
        break

if found == True:
    print(num, "encontrado")
else:
    print(num, "no encontrado")

print("EJERCICIO 7")
print("1. Mensaje de buenos días\n2. Mensaje de buenas tardes\n3. Mensaje de buenas noches\n0. Salir")
print("----------------")
while True:
    option = int(input())
    if option == 1:
        print("Buenos días! :)")
    elif option == 2:
        print("Buenas tardes! :D")
    elif option == 3:
        print("Buenas noches! ;)")
    elif option == 0:
        print("Adiós...")
        break
    else:
        print("Opción inválida")