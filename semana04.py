# Dos listas para trabajar
"""equipos = ["Ada", "Turing", "Grace", "Linus"]
puntajes = [82, 95, 76, 88]
contador = 0

for equipo in equipos:
    print(f"{contador+1}. {equipos[contador]}")
    contador = contador + 1"""

"""lenguajes = ["Python", "C#", "JavaScript"]
print(f"Lenguajes de programación actuales son: {lenguajes}")
lenguaje_nuevo = input("Digite el nuevo lenguaje de programación: ")
lenguajes.append(lenguaje_nuevo)"""


"""for i in range(1, 7, 2):
    print(i)"""

"""print(list(range(1, 11)))"""

"""a = list(range(1, 6))
b = list(range(1, 10, 2))
c = list(range(3, 19, 3))

print(a)
print(b)
print(c)"""

equipos = ["Ada", "Turing", "Grace", "Linus"]
puntajes = [82, 95, 76, 88]
puntaje_mínimo = int(input("Digite el puntaje mínimo: "))
index = 0
bonificados = []
puntajes_aprobados = []
equipos_aprobados = []

"""for puntaje in puntajes:
    nuevo = puntaje + 5
    bonificados.append(nuevo)

print(bonificados)"""

for puntaje in puntajes:
    if puntaje > puntaje_mínimo:
        print(puntaje)
        equipos_aprobados.append(equipos[index])
    index += 1

print(equipos_aprobados)
