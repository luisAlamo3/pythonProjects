# Solicitamos la cantidad de ciudadanos que realizarán una solicitud
cantidad_ciudadanos = int(input("Ingrese la cantidad de ciudadanos que realizarán una solicitud: "))

# Creamos una lista para almacenar las solicitudes de cada ciudadano
solicitudes = []

# Solicitamos la información de cada ciudadano
for i in range(cantidad_ciudadanos):
    print(f"\nCiudadano {i + 1}:")
    nombre = input("Ingrese su nombre: ")
    tiempo_estimado = int(input("Ingrese el tiempo estimado en minutos (max 120 min): "))
    
    ciudadano = {
        "id": i + 1,
        "nombre": nombre,
        "tiempo_estimado": tiempo_estimado
    }
    # Agregamos el diccionario a la lista de solicitudes
    solicitudes.append(ciudadano)

# Ordenamos las solicitudes por tiempo estimado
#solicitudes.sort(key=lambda x: x['tiempo_estimado'])
# Ordenamos las solicitudes por tiempo estimado con el metodo burbuja
for i in range(len(solicitudes) - 1):
    for j in range(len(solicitudes) - 1 - i):
        if solicitudes[j]['tiempo_estimado'] > solicitudes[j + 1]['tiempo_estimado']:
            solicitudes[j], solicitudes[j + 1] = solicitudes[j + 1], solicitudes[j]

# Mostramos la lista de solicitudes ordenadas
print("\nLista de Solicitudes Ordenadas:")
for ciudadano in solicitudes:
    print(f"Ciudadano {ciudadano['id']}: {ciudadano['nombre']} - {ciudadano['tiempo_estimado']} minutos")

