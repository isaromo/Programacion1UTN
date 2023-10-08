print("\nEJERCICIO 1")
word = input("Ingrese una palabra: ")
for i in range(0,10):
    print(word)

print("\nEJERCICIO 2")
age = int(input("Ingrese su edad: "))
for i in range(1,age+1):
    print(i)


print("\nEJERCICIO 3")
num = int(input("Ingrese un número entero positivo: "))
for i in range(1,num+1):
    if i%2 != 0: #si es impar se imprime el num
        if i == num or i == num-1: #si el num es el último o el penúltimo...
            print(i) #...no se muestra la coma
        else:
            print(i, end = ", ") #sino, se muestra la coma

print("\nEJERCICIO 4")
num = int(input("Ingrese un número entero positivo: "))
for i in range(0,num+1):
    if num-i == 0:
        print(num-i)
    else:
        print(num-i, end=", ")

print("\nEJERCICIO 5")
inv = int(input("Ingrese la cantidad a invertir: "))
interest = float(input("Ingrese el interés anual: "))
interest = interest / 100
years = int(input("Ingrese la duración de la inversión: "))
for i in range(0,years):
    inv += inv*interest
    print("**AÑO ", 2023+i, "**") #muestra el año
    print("Capital obtenido: $", inv) #muestra el total de la inv + lo ganado

print("\nEJERCICIO 6")
number = int(input("Ingrese la altura: "))

for i in range(1,number+1):
    counter = i
    for q in range(1,counter+1):
        print("*", end="")
    print("")

print("\nEJERCICIO 7")
for i in range(1,11):
    print("1 x ", i, " = ", i)

print("\nEJERCICIO 9")
passw = "admin123"
while True:
    pass_inp = input("Ingrese la contraseña: ")
    if pass_inp in passw:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta\n")

print("\nEJERCICIO 10")
number = int(input("Ingrese un num entero: "))
dividers = 0

for i in range(1,number+1):
    if number%i == 0:
        dividers += 1

if dividers > 2:
    print("No es primo")
else:
    print("Es primo")