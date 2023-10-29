from TP7_functions import show_array, bubble_sort, selection_sort
'''
#EJERCICIO 1
print("Ingrese 10 números")
counter = 0
numbers = []

while counter < 10:
    numbers.append(int(input()))
    counter += 1

show_array(numbers)
print("Lista ordenada:")
numbers = bubble_sort(numbers)
show_array(numbers)

#EJERCICIO 2
print("Ingrese 10 cadenas")
counter = 0
strings = []

while counter < 10:
    strings.append(input())
    counter += 1

show_array(strings)
print("Lista ordenada:")
strings = selection_sort(strings)
show_array(strings)
'''
#EJERCICIO 4
print("Ingrese 7 cadenas")
counter = 0
strings2 = []

while counter < 7:
    strings2.append(input())
    counter += 1