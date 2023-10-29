'''Función ejercicio 1'''
def valid_dni(dni):
    if len(str(dni)) < 7 or len(str(dni)) > 8:   #convierto el dni a string para poder contar la longitud
        return False  #el dni no está entre 7 y 8, no es válido y se retorna falso
    else:
        return True
    
'''Función ejercicio 2'''    
def last_word_length(phrase):
    phrase = phrase[::-1]   #doy vuelta la frase para encontrar más fácil la última palabra
    word_length = len(phrase[:phrase.find(" ")])   #extraigo la última palabra y saco la longitud
    return word_length

'''Función ejercicio 4'''
def multiple_or_not(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

'''Función ejercicio 5'''
def average_temperature(max_t, min_t):
    return (max_t + min_t) / 2

'''Función ejercicio 6'''
def separate_words(phrase):
    return " ".join(list(phrase))   #uso el método join para agregarle un espacio entre cada caracter, dentro del parentesis convierto al string en una lista para que pueda mutarse

'''Función ejercicio 7'''
def highest_lowest(numbers):
    highest = 0
    counter = 0 #contador para que en la primera iteración del for se asigne ese valor de N como el menor

    for n in numbers:
        if counter == 0:
            lowest = n
            counter = 1 #incremento el contador para que ya no vuelva a ingresar a este if
        
        if n > highest:
            highest = n
        
        if n < lowest:
            lowest = n

    print("MAYOR: ", highest, "\nMENOR: ", lowest)

'''Función ejercicio 8'''
def area_perimeter(radius):
    print("PERÍMETRO: ", 2 * 3.14 * radius) 
    print("ÁREA: ", 3.14 * (radius*radius))

'''Función ejercicio 9'''
def login(user, password):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        return False

'''Función ejercicio 10'''
def discounts(shopping_cart):
    summation = 0
    for k, v in shopping_cart.items():
        v /= 100    #convierto lo que el usuario ingresaría como, por ej, 50 (50% de descuento), a 0.50 para poder hacer la cuenta del descuento más facilmente
        k -= k * v  #al precio le resto el descuento
        summation += k
    
    return summation


'''Función ejercicio 11 '''
def area_circle(radius):
    return 3.14 * (radius*radius)

def ejercicio11(area_circle, radiuses):
    calculated_radiuses = []
    for r in radiuses:
        r = area_circle(r)
        calculated_radiuses.append(r)
    
    return calculated_radiuses

'''Función ejercicio 12'''
def phrase_to_dictionary(phrase):
    start = 0
    dictionary = {}

    for i in range(0, len(phrase)):
        if phrase[i] == " ":    #si phrase[i] es un espacio, entonces lo anterior es una palabra.
            word = phrase[start : i]    #obtengo la palabra desde la posición de comienzo hasta el espacio
            start = (i+1)     #reseteo la posición de comienzo a ese espacio encontrado

            dictionary[word] = len(word)

        elif i == (len(phrase)-1):    #También considero el caso de que en vez de un espacio, sea el final de la oración (es decir i == longitud de la frase (menos 1))
            word = phrase[start : i+1]
            dictionary[word] = len(word)
    
    return dictionary

'''Función ejercicio 13'''
def module(array):
    result = 0
    for i in array:
        result += (i * i)
    
    return result * (1/2)

'''Función ejercicio 14'''
def prime_or_not(number):
    counter = 0
    prime = True

    for i in range(1, number+1):    #for para poder dividir al número desde 1 hasta sí mismo
        if number % i == 0:
            counter += 1

        if counter > 2:
            prime = False
            break
    
    return prime

'''Función ejercicio 15'''
def all_factorials(num_array):
    for number in num_array:    #para imprimir el factorial de cada num en el array
        print(f"\n----- FACTORIAL DE {number}-----")
        print(f"!{number} = ", end = "")

        for i in reversed(range(1, number+1)):  #invierto el range para que se muestre de mayor a menor (5 * 4 * 3...)
            if  i == 1 and factorial(number) == 1:  #if para que al imprimir el factorial de 1, se muestre '!1 = 1" en vez de '!1 = 1 = 1'
                print("", end= "")
            elif i == 1:
                print(i, end= " = ")
            else:
                print(i, end = " * ")

        print(factorial(number))
    
    return "\nAdiós!"


'''Función 2 ejercicio 15'''
def factorial(n):   #para calcular el factorial
    result = n
    if n == 0:
        result = 1
    else:
        result *= factorial(n-1)

    return result

'''Función ejercicio 16'''
def digit_in_num(num, dig):
    counter = 0
    for n in str(num):  #convierto el número a string para poder iterarlo
        if int(n) == dig:   #convierto el elemento a int para poder compararlo con el dígito
            counter += 1
    
    print(f"El número {dig} se encuentra {counter} vez/veces en el número {num}")


def sum_digits(n):
    sum = 0

    while n > 0:
        digit = n % 10
        n = n // 10
        sum += digit
    
    return sum