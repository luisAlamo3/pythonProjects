import random

# Datos preestablecidos para pruebas rápidas
usar_datos_prueba = True  # Cambia a True para usar datos de prueba

nombres_base = [
    "Ana", "Luis", "Carlos", "María", "José", "Elena", "Pedro", "Lucía", "Miguel", "Sofía",
    "Juan", "Laura", "Andrés", "Paula", "Diego", "Valeria", "Jorge", "Camila", "Fernando", "Daniela",
    "Ricardo", "Gabriela", "Raúl", "Patricia", "Roberto", "Sandra", "Alberto", "Mónica", "Hugo", "Carmen",
    "Manuel", "Rosa", "Francisco", "Teresa", "Guillermo", "Alicia", "Eduardo", "Beatriz", "Felipe", "Verónica",
    "Oscar", "Silvia", "Martín", "Isabel", "Pablo", "Natalia", "Emilio", "Lorena", "Tomás", "Julia"
]

datos_prueba = [
    {
        "nombre": f"{random.choice(nombres_base)}_{i+1}",
        "tiempo_estimado": random.randint(10, 120)
    }
    for i in range(5000)
]

solicitudes = []

if usar_datos_prueba:
    for i, dato in enumerate(datos_prueba):
        ciudadano = {
            "id": i + 1,
            "nombre": dato["nombre"],
            "tiempo_estimado": dato["tiempo_estimado"]
        }
        solicitudes.append(ciudadano)
    cantidad_ciudadanos = len(datos_prueba)
else:
    # Solicitamos la cantidad de ciudadanos que realizarán una solicitud
    cantidad_ciudadanos = int(input("Ingrese la cantidad de ciudadanos que realizarán una solicitud: "))

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

