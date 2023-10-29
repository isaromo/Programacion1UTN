from TP8_functions import return_positions, odd, return_digits, validate_power, highest_num, repeat_list
'''
#EJERCICIO 1
number = int(input("Ingrese un número positivo: "))
print(f"{number} tiene {return_digits(number)} dígito/s")

#EJERCICIO 2
n = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
result = validate_power(n,b)
if result == False:
    print(f"¿Es {n} potencia de {b}? {result}")
else:
    print(f"¿Es {n} potencia de {b}? {result[0]} -> {b} ^ {result[1]} = {n}")

#EJERCICIO 3
phrase = input("Ingrese una frase: ")
substring = input("Ingrese una cadena a buscar: ")
print(return_positions(phrase,substring))

#EJERCICIO 4
number = int(input("Ingrese un número: "))
print(f"¿Es {number} impar? ", odd(number))

#EJERCICIO 5
list = [1,8,4,7,21,3,6,9,10,2]
print(f"El mayor es: {highest_num(list)}")
'''