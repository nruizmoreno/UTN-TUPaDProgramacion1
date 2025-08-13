# # EJERCICIO 1
# print("Hola mundo")

# # EJERCICIO 2
# nombre = input("Ingrese su nombre: ")
# print(f"Hola {nombre}")

# # EJERCICIO 3
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = int(input("Ingrese su edad: "))
# reseidencia = input("Ingrese su lugar de residencia: ")
# print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {reseidencia}.")

# EJERCICIO 4
# radio = float(input("Ingrese el radio de un circulo para obtener su area y su perimetro: "))
# PI = 3.14
# area = radio * radio * PI 
# perimetro = 2 * PI * radio
# print(f"El area del circulo es {round(area, 2)}, y el perimetro es {round(perimetro, 2)}.")

# EJERCICIO 5
# segundos = int(input("Ingrese la cantidad de segundos para obtener el equivalente en horas: "))
# horas = segundos / 3600
# print(f"{segundos} equivale a {round(horas, 2)}"

# EJERCICIO 6
# num = int(input("Ingrese un numero para obtener su tabla de multiplicacion: "))
# acu = 0
# print(f"Tabla de multiplicar del numero {num}")
# while acu < 13:
#     prod = num * acu
#     print(f"{num} * {acu} = {prod}")
#     acu += 1

# EJERCICIO 7
# num1 = int(input("Ingrese el primer numero, debe ser entero distinto de cero: \n"))
# while num1 == 0:
#     print("Error, el numero debe ser distinto de cero, ingrese otro numero por favor: ")
#     num1 = int(input("Ingrese el primer numero, debe ser entero distinto de cero: \n"))

# num2 = int(input("Ingrese el segundo numero, debe ser entero distinto de cero: \n"))
# while num2 == 0:
#     print("Error, el numero debe ser distinto de cero, ingrese otro numero por favor: ")
#     num2 = int(input("Ingrese el segundo numero, debe ser entero distinto de cero: \n"))
# print(f"Operaciones con {num1} y {num2}: \n Suma: {num1 + num2}, \n Resta: {num1 - num2}, \n Multiplicacion: {num1 * num2}, \n Division: {round(num1 / num2, 2)}.")

# EJERCICIO 8
# altura = float(input("Ingrese su altura en metros: \n"))
# peso = float(input("Ingrese su peso en kilos: \n"))

# imc = round(peso / altura, 2)
# print(f"Su indice masa corporal es: {imc}.")

# EJERCICIO 9
# celsius = int(input("Ingrese la temperatura en grados Celsius para obtenerla en Farenheit: \n"))
# farenheit = 9/5 * celsius + 32
# print(f"{celsius} grados Celsius equivale a {farenheit} grados Farenheit.")

# EJERCICIO 10
# print("Ingrese tres numeros para obtener el promedio de la suma... \n")
# num1 = float(input("Ingrese el primer numero: \n"))
# num2 = float(input("Ingrese otro numero: \n"))
# num3 = float(input("Ingrese otro numero: \n"))
# promedio = (num1 + num2 + num3) / 3
# print(f"El promedio de sumar {num1}, {num2} y {num3} es igual a {promedio}.")
