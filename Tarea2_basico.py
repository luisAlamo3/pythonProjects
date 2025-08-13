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