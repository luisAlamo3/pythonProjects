# Devuelve la primera letra y la vocal siguiente del apellido paterno
def obtener_iniciales(apellido):
    inicial = apellido[0]
    for letra in apellido[1:]:
        if letra in 'aeiouAEIOU':
            return inicial.upper() + letra.upper()
    return inicial.upper() + 'X'  # Si no hay vocal, devuelve 'X'

def obtener_iniciales_materno(apellido):
    return apellido[0].upper()

def obtener_fecha_nacimiento(fecha):
    anio = fecha.split("/")[2]
    mes = fecha.split("/")[1]
    dia = fecha.split("/")[0]
    return f"{anio[2:]}{mes}{dia}"

def obtener_sexo(genero):
    return 'H' if genero.lower() == 'masculino' else 'M'

def obtener_ciudad(ciudad):
    ciudades = {
        "Ciudad de México": "DF",
        "Guadalajara": "JA",
        "Monterrey": "NL",
        "Puebla": "PU",
        "Tijuana": "BC"
    }
    return ciudades.get(ciudad, ciudad[:2].upper())

# Primera consonante interna del primer apellido.
def obtener_consonante_interna(apellido):
    consonantes = [letra.upper() for letra in apellido if letra.upper() not in 'AEIOU']
    return consonantes[1] if len(consonantes) > 1 else 'X'


print(obtener_iniciales("Alamo"))
print(obtener_iniciales_materno("Ramos"))
print(obtener_iniciales_materno("Luis"))
print(obtener_fecha_nacimiento("15/08/1990"))
print(obtener_sexo("Masculino"))
print(obtener_ciudad("Ciudad de México"))
print(obtener_consonante_interna("Alamo"))