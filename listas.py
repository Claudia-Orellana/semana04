"""nombre = "Javier"
print(len(nombre))"""

# artículo = "Cuaderno"
# números = [1, 4, 10, 20, 47]

"""Aquí estamos creando objetos"""
variable = "alumno"

productos = []

# estaría mal porque aparece antes de que se le asigne cuaderno a la lista. SECUENCIA IMPORTA
print(
    f"La cantidad de Cuaderno dentro de producto es {productos.count("Cuaderno")}")

"""Aquí los estamos procesando"""
productos.append("Lapicero")
productos.append("Cuaderno")
productos.append("Mochila")
productos.append("Botella")

# productos = ["Lapicero", "Cuaderno", "Mochila", "Botella"]
# persona1 = ["Alvin", 40, "Economista", 166.23, ["Mariana", "María José"]]

"""print(type(artículo))
print(type(números))
print(type(productos))"""

"""print(len(productos))
print(productos[-3])"""

print(
    f"La cantidad de Cuaderno dentro de producto es {productos.count("Cuaderno")}")

"""indice = input("Digite el indice a consultar [1-3]: ")

print(
    f"El primer elemento de la lista productos es {productos[int(indice)-1]}")"""

"""while True:
    # articulo = input("Digite el artículo a ingresar (Salir para salir): ").capitalize()
    posición = int(input("Digite la posición a donde lo vamos a insertar: "))-1
    if posición == "Salir":
        break
    else:
        del productos[posición]
        print(f"La lista de artículos disponibles es {productos}")"""

# para hacer que se quede el valor que le ingresemos, lo que hicimos ahi fue hacer un bucle infinito para que siempre pregunte
# pero lo más óptimo sería hacer un bucle/condicional que se rompa cuando el usuario quiera, por ejemplo, "salir"

"""articulo_borrado = productos.pop(1)
print(f"La lista de artículos disponibles es {productos}")
print(f"El artículo borrado es {articulo_borrado}")"""

print(sorted(productos))
print(productos)
