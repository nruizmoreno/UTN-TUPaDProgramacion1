# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
acu = 0
numero = int(input("Ingrese un número entero, ser determinara la cantidad de dígitos que contiene: \n"))
while numero > 0:
    acu += 1
    numero //= 10
print(acu)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
acu = 0
print("Se sumaran todos los números enteros comprendidos entre el rango que usted especifique, sin incluir los"
      " límites.")
num1 = int(input("Ingrese el límite inferior: \n"))
num2 = int(input("Ingrese el límite superior: \n"))
for i in range(num1 + 1, num2, 1):
    acu += i
    print(acu)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
acu = 0
print("Ingrese, uno por uno, los números que quiera sumar. Para terminar, ingrese el número 0:")
num = int(input("Ingrese el primer número:\n"))
while num != 0:
    acu += num
    num = int(input("Ingrese, otro número:\n"))
print(acu)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
from random import randint

intentos = 1
num_random = randint(0,9)
num_user = int(input("Adivine un número entero entre 0 y 9, incluidos: \n"))

while num_user != num_random:
    intentos += 1
    print("Incorrecto...inténtelo de nuevo: \n")
    num_user = int(input("Adivine un número entero entre 0 y 9, incluidos: \n"))

if intentos == 1:
    print(f"Correcto! el número era: {num_random}.\nUsted realizó un solo intento para adivinar el número. "
          f"Felicitaciones!")
else:
    print(f"Correcto! el número era: {num_random}.\nUsted realizó {intentos} intentos para adivinar el número.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
acu = 0
num = int(input("Ingrese un número entero positivo, para calcular la suma de todos los números comprendidos entre 0 y"
                " el número ingresado (excluyente):\n"))
for i in range(0, num, 1):
    acu += i
print(acu)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
acu_pares = 0
acu_impares = 0
acu_positivos = 0
acu_negativos = 0

print("Ingrese 100 números enteros, para saber cuántos de estos números son pares, cuántos son impares, cuántos son positivos y cuántos son negativos.")
num_user = int(input("Ingrese el primero número:\n"))

for i in range(0, 100):
    if num_user % 2 == 0:
        acu_pares += 1
    else:
        acu_impares += 1

    if num_user > 0:
        acu_positivos += 1
    else:
        acu_negativos += 1
    num_user = int(input("Ingrese otro número:\n"))

print(f"Resultados:\nTotal números pares: {acu_pares}.\nTotal números impares: {acu_impares}.\nTotal números positivos: "
      f" {acu_positivos}.\nTotal números negativos: {acu_negativos}.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
acu = 0
print("Ingrese 100 números enteros. Se calculara la media de dichos valores.")


for i in range(0, 100):
    if i == 0:
        num_user = int(input("Ingrese el primero número:\n"))
    else:
        num_user = int(input("Ingrese otro número:\n"))
    acu += num_user

print(f"La media de la suma de todos los números ingresados es: {acu / 100}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num_user = int(input("Ingrese un número: \n"))
num_original = num_user
num_invertido = 0

while num_user > 0:
    ultimo_digito = num_user % 10
    num_invertido = (num_invertido * 10) + ultimo_digito
    num_user //= 10

print(f"El número ingresado fue: {num_original}, y su inverso es: {num_invertido}.")
