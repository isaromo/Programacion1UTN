from TP6_functions import show_array

#EJERCICIO 1
print("Ingrese nums. Para salir ingrese 0")
num_array = []

while True:
    num = int(input())
    if num == 0:
        break

    num_array.append(num)

show_array(num_array)

#EJERCICIO 2
number = int(input("Ingrese un número a remover en la lista: "))
if number in num_array:
    num_array.remove(number)
else:
    print(f"{number} no se encuentra en la lista")

show_array(num_array)

#EJERCICIO 3
summation = 0
for n in num_array:
    summation += n

print("\nSumatoria de la lista: ", summation)

#EJERCICIO 4
lower_numbers = []
number2 = int(input("Ingrese un número. Se creará una nueva lista con los elementos de la lista original menores a este: "))

for n in num_array:
    if n < number2:
        lower_numbers.append(n)

show_array(lower_numbers)

#EJERCICIO 5
print("Ocurrencias de cada elemento en la lista original: ")
num_quant = []
repeated = []

for n in num_array:
    if n not in repeated:
        num_quant.append((n, num_array.count(n)))
    
    repeated.append(n)  # agrego el elemento a otro array para poder verificar que al array de cantidades no se le agregue más de una vez el mismo número

show_array(num_quant)