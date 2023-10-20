from functions_ejPower import *

num = int(input("Ingrese numero: "))
summation_num = 0
summation_digit = 0

while num!=0:
    print(f"Suma de digitos: {sum_digits (num)}")
    summation_num += num
    num = int(input("Ingrese numero: "))

summation_digit = sum_digits(summation_num)
print(f"Suma de numeros: {summation_num}")
print(f"Suma de digitos: {summation_digit}")