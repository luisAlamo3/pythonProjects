pGanados = 0
pEmpatados = 0
pPerdidos = 0
nombreEquipo = ""

pGanados = int(input("Introduce el numero de partidos ganados: "))
pEmpatados = int(input("Introduce el numero de partidos empatados: "))
pPerdidos = int(input("Introduce el numero de partidos perdidos: "))

nombreEquipo = input("Introduce el nombre del equipo: ")

print("El equipo ", nombreEquipo, " tiene: ", (pGanados*3)+(pEmpatados*1)+(pPerdidos*0), " puntos")