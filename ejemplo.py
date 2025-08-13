# # Ejemplo de uso de condicionales en Python
# letra = "";
# letra = input("Introduce una letra: ");
# letra = letra.upper();
# if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
#     print("La letra es una vocal")
# else:
#     print("La letra es una consonante")

# # Ejemplo de uso de condicionales y bucles en Python
# total = 0
# total = int(input("Introduce el total de la compra: "))
# if total >= 1000:
#     total = total * 0.90

# print("El total a pagar es: ", total)

# # Ejemplo de uso de bucles en Python
# # Tabla de multiplicar del número introducido por el usuario
# numero = 0
# numero = int(input("¿Qué tabla de multiplicar quieres ver? "))
# contador = 1
# while contador <= 10:
#     resultado = numero * contador
#     print(numero, "x", contador, "=", resultado)
#     contador += 1
# print("Fin de la tabla de multiplicar del", numero)

# Ejemplo de uso de listas y bucles en Python

# calificaciones = [6,7,8,10,5]
# suma = 0
# promedio = 0

# for calificacion in calificaciones:
#     suma = suma + calificacion

# promedio = suma / len(calificaciones)
# print("El promedio de las calificaciones es:", promedio)"""

# # Ejemplo de uso de condicionales y bucles en Python
# # Simulador de cajero automático
# saldo = 2000
# valor = True
# menu = """
# 1. Consultar saldo
# 2. Depositar
# 3. Retirar
# 4. Salir
# """

# while valor:
#     print(menu)
#     opcion = int(input("Selecciona una opción: "))
    
#     if opcion == 1:
#         print("Tu saldo es:", saldo)
#     elif opcion == 2:
#         deposito = float(input("¿Cuánto deseas depositar? "))
#         saldo += deposito
#         print("Depósito exitoso. Tu nuevo saldo es:", saldo)
#     elif opcion == 3:
#         retiro = float(input("¿Cuánto deseas retirar? "))
#         if retiro > saldo:
#             print("Saldo insuficiente para realizar el retiro.")
#         else:
#             saldo -= retiro
#             print("Retiro exitoso. Tu nuevo saldo es:", saldo)
#     elif opcion == 4:
#         print("Gracias por usar el sistema. ¡Hasta luego!")
#         valor = False
#     else:
#         print("Opción no válida, por favor intenta de nuevo.")

# Ejemplo de uso de funciones en Python
# Imprime las tablas de multiplicar del 1 al 5
# def tabla_multiplicar(numero):
#     print("Tabla de multiplicar del", numero)
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")
#     print("Fin de la tabla de multiplicar del", numero)

# for num in range(1, 6):
#     tabla_multiplicar(num)

# Ejemplo de uso de bucles en Python
# # Imprime las tablas de multiplicar del 1 al 5 usando un bucle while
# tablas = [1, 2, 3, 4, 5]
# j = 0
# print("Tablas de multiplicar del 1 al 5:")
# print("====================================")

# while j < len(tablas):
#     print("Tabla de multiplicar del", tablas[j])
#     for i in range(1, 11):
#         resultado = tablas[j] * i
#         print(f"{tablas[j]} x {i} = {resultado}")
#         print(tablas[j], "x", i, "=", resultado)
#     j += 1

# print("Fin de las tablas de multiplicar del 1 al 5")

# Ejemplo de uso de listas y bucles en Python
# Adivina el número secreto
import random

numero_secreto = random.randint(1, 100)
intentos = 0
print("Bienvenido al juego de adivinar el número secreto.")
print("He seleccionado un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")
while intentos < 10:
    try:
        adivinanza = int(input("Introduce tu adivinanza: "))
        intentos += 1
        
        if adivinanza < numero_secreto:
            print("Demasiado bajo. Inténtalo de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Inténtalo de nuevo.")
        else:
            print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
            break
    except ValueError:
        print("Por favor, introduce un número válido.")

if intentos == 10:
    print(f"Lo siento, has agotado tus intentos. El número secreto era {numero_secreto}.")
