# 1. Planeación
# Inicio
# Solicitar la cantidad de ciudadanos que se atenderán
# Para cada solicitud:
# Registrar nombre
# Registrar tiempo estimado

# si la cantidad de solicitudes aun no es la que se indico al principio sigue solicitando
# si la cantidad de solicitudes es la que se indico finaliza la solicitud de registro

# manda a ordenar las solicitudes por tiempo estimado de menor a mayor

# mostrar la lista ordenada.

# Fin

# 2. Análisis
# Entrada de datos:
# La cantidad máxima de ciudadanos que serán atendidos será de 100 
# Cada solicitud deberá tener un nombre (máximo 50 caracteres) y un 
# Tiempo estimado de atención (máximo 120 minutos)

# Proceso:
# Se deberán ordenar las solicitudes de menor a mayor

# Salida esperada:
# Una lista de solicitudes (nombre y tiempo de espera estimado) ordenada de menor a mayor por tiempo de espera estimado

# 3. Diseño de Solución
# Inicio
# Solicitar la cantidad de ciudadanos que se atenderán
# generar una lista de dicha cantidad
# Para cada solicitud:
# Registrar nombre
# Registrar tiempo estimado
# Guardar cada solicitud en un bloque de la lista
# si la cantidad de solicitudes aun no es la que se indico al principio sigue solicitando
# si la cantidad de solicitudes es la que se indicó deja de pedir solicitudes

# manda a ordenar las solicitudes por tiempo estimado de menor a mayor

# mostrar la lista ordenada.

# Fin


# Versión básica: ingreso manual y sin medición de tiempo

solicitudes = []

cantidad_ciudadanos = int(input("Ingrese la cantidad de ciudadanos que realizarán una solicitud: "))

for i in range(cantidad_ciudadanos):
    print(f"\nCiudadano {i + 1}:")
    nombre = input("Ingrese su nombre: ")
    tiempo_estimado = int(input("Ingrese el tiempo estimado en minutos (max 120 min): "))
    ciudadano = {
        "id": i + 1,
        "nombre": nombre,
        "tiempo_estimado": tiempo_estimado
    }
    solicitudes.append(ciudadano)

# Ordenamiento burbuja por tiempo estimado
for i in range(len(solicitudes) - 1):
    for j in range(len(solicitudes) - 1 - i):
        if solicitudes[j]['tiempo_estimado'] > solicitudes[j + 1]['tiempo_estimado']:
            solicitudes[j], solicitudes[j + 1] = solicitudes[j + 1], solicitudes[j]

print("\nLista de Solicitudes Ordenadas:")
for ciudadano in solicitudes:
    print(f"Ciudadano {ciudadano['id']}: {ciudadano['nombre']} - {ciudadano['tiempo_estimado']} minutos")