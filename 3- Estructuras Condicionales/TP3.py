# ACTIVIDADES
# 1)

edad = int(input("Ingrese su edad para saber si es mayor de edad: \n"))
if edad > 18:
    print("Usted es mayor de edad.")
elif edad <= 18 and edad > 0:
    print("Usted es menor de edad.")
else:
    print("Valor incorrecto, ingrese una edad válida.")

# 2)

nota = int(input("Ingrese la nota recibida para saber si aprobó o no: \n"))
if nota >= 6 and nota <= 10:
    print("Aprobado")
elif nota >=1 and nota < 6:
    print("Desaprobado")
else:
    print("Valor incorrecto, ingrese una nota válida.")

# 3)

no_es_par = True
while  no_es_par:
    num = float(input("Ingrese un número par: \n"))
    if num % 2 == 0:
        print("Ha ingresado un número par!")
        no_es_par = False
    else:
        print("Por favor, ingrese un número par")

# 4)
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad para ver a cuál categoría pertenece \n"))
if edad > 0 and edad < 12:
    print("Usted pertenece a la categoría niño.")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoría adolescente.")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoría Adulto/a joven.")
elif edad >= 30:
    print("Usted pertenece a la categoría Adulto/a.")
else:
    print("Valor incorrecto, ingrese una edad válida.")

# 5)

password_ok = False
while not password_ok:
    password = input("Ingrese una contraseña que contenga entre 8 y 12 caracteres. (inclusive) \n")
    if len(password) >= 8 and len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
        password_ok = True
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)
# moda: valor mas comun de datos discretos o nominales:
# mediana: valor central de los datos.
# media: promedio de los datos.

import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print(f"media = {media}, mediana = {mediana}, moda = {moda}")
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print(f"media = {media}, mediana = {mediana}, moda = {moda}")
    print("Sesgo negativo o a la izquierda")
elif media == mediana and media == moda:
    print(f"media = {media}, mediana = {mediana}, moda = {moda}")
    print("Sin sesgo.")
else:
    print(f"media = {media}, mediana = {mediana}, moda = {moda}")
    print("Sesgo no especificado por el ejercicio.")

# 7)

vocales = "aeiou"
frase = input("Ingrese una frase o palabra: \n")
if frase[-1].lower() in vocales:
    print(f"{frase}!")
else:
    print(frase)

# 8)

run_code = True
nombre = input("Ingrese su nombre: \n")

while run_code:
    menu = int(input("Seleccione la opción deseada: \n [1] Si quiere su nombre en mayúsculas, \n [2] Si quiere su nombre en minúsculas, \n [3] Si quiere su nombre con la primera letra mayúscula. \n"))
    if menu == 1:
        print(nombre.upper())
        run_code = False
    elif menu == 2:
        print(nombre.lower())
        run_code = False
    elif menu == 3:
        print(nombre.title())
        run_code = False
    else:
        print("La opción ingresada no es válida, ingrese otro número.")

# 9)

run_code = True
magnitud = int(input("Ingrese la magnitud de un terremoto: \n"))

while run_code:
    if 1 <= magnitud < 3:
        print("Muy leve (imperceptible)")
        run_code = False
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible).")
        run_code = False
    elif 4 <= magnitud < 5:
        print("Fuerte (puede causar daños en estructuras débiles).")
        run_code = False
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos).")
        run_code = False
    elif magnitud >= 7:
        print("Extremo (puede causar graves daños a gran escala).")
        run_code = False
    else:
        print("El número ingresado esta afuera de la escala de Richter (debe ser un entero positivo), ingrese otro número.")
        magnitud = int(input("Ingrese la magnitud de un terremoto: \n"))

# 10)
# codigo para verificar si los datos ingresados por el usuario son validos.
run_code_hemisferio = True
run_code_mes = True
run_code_dia = True

# organización de meses según la cantidad de días que tienen, 30 o 31.
# También se crea un string vacío para la variable estación.
meses_31_dias = [1,3,5,7, 8,10,12]
meses_30_dias = [2,4,6,7,9,11]
estacion = ""

# Ingreso y validación de datos
while run_code_hemisferio:
    hemisferio = input("En qué hemisferio se encuentra? (norte o sur)").lower()
    if hemisferio == "norte" or hemisferio == "sur":
        run_code_hemisferio = False

while run_code_mes:
    mes = int(input("En qué mes del año (número del mes)?"))
    if 1 <= mes <= 12:
        run_code_mes = False

while run_code_dia:
    dia = int(input("En qué día? (número)"))
    if mes in meses_31_dias:
        if dia > 31 or dia < 1:
            print("El número es incorrecto. Ingresar nuevamente el día. El mes ingresado tiene 31 días.")
        else:
            run_code_dia = False
    elif mes in meses_30_dias:
        if dia >30 or dia < 1:
            print("El número es incorrecto. Ingresar nuevamente el día. El mes ingresado tiene 30 días.")
        else:
            run_code_dia = False

# Condicionales organizados según la tupla fecha: mes y dia.
fecha = (mes, dia)
if ((12, 21) <= fecha <= (12, 31)) or (1, 1) <= fecha <= (3, 20):
    if hemisferio == "norte":
        estacion = "Invierno"
    elif hemisferio == "sur":
        estacion = "Verano"
elif (3, 21) <= fecha <= (6, 20):
    if hemisferio == "norte":
        estacion = "Primavera"
    elif hemisferio == "sur":
        estacion = "Otoño"
elif (6, 21) <= fecha <= (9, 20):
    if hemisferio == "norte":
        estacion = "Verano"
    elif hemisferio == "sur":
        estacion = "Invierno"
elif (9, 21) <= fecha <= (12, 20):
    if hemisferio == "norte":
        estacion = "Otoño"
    elif hemisferio == "sur":
        estacion = "Primavera"

print(f"Usted se encuentra en la siguiente estación: {estacion}.")
