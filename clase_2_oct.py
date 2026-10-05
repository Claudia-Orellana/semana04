# sistema de control de colas
print('Bienvenido al sistema')
cola = ["Sofía", "Mateo", "Valeria"]
cancelados = []
print(f"La cola actual es: {cola}")
print("Menu")
print("1. Registrar estudiante regular")
print("2. Registrar estudiante prioritario")
print("3. Cancelar una solicitud")
print("4. Atender al siguiente estudiante")
print("5. Consultar la cola")
print("6. Cerrar el sistema")

"""opcion = int("2")
print(opcion)"""

opcion = input("Elija una opción (1 - 6): ")
while True:
    if opcion == "1":
        while True:
            estudiante = input(
                "Digite el nombre del estudiante (Ej. Juan): ").capitalize()
            if estudiante == "" or estudiante in cola:
                print("El nombre es inválido")
            else:
                cola.append(estudiante)
                print(f"La nueva cola es : {cola}")
                break
    elif opcion == "2":
        while True:
            estudiante = input(
                "Digite el nombre del estudiante (Ej. Juan): ").capitalize()
            if estudiante == "" or estudiante in cola:
                print("El nombre es inválido")
            else:
                cola.insert(0, estudiante)
                print(f"La nueva cola es : {cola}")
                cancelados.append(estudiante)
                print(f"La cola de cancelados es: {cancelados}")
                break
    elif opcion == "3":
        while True:
            estudiante = input(
                "Digite el nombre del estudiante a cancelar (Ej. Juan): ").capitalize()
            if estudiante == "" or estudiante not in cola:
                print("El nombre es inválido")
            else:
                cola.remove(estudiante)
                cancelados.append(estudiante)
                print(f"La nueva cola es : {cola}")
                print(f"La cola de cancelados es: {cancelados}")
                break
    elif opcion == "4":
        if cola == []:
            print("Cola vacía, no hay estudiantes para atender.")
        else:
            atendido = cola.pop(0)
            cancelados.append(atendido)
            print(f"Estudiante atendido: {atendido}")
            print(f"La nueva cola es : {cola}")
    elif opcion == "6":
        confirmacion = input("Esta seguro (Y/N)?")
        if confirmacion == "Y":
            print("Gracias por venir.")
            print(f"La lista actual es: {cola}")
            print(f"La cola de cancelados es: {cancelados}")
            break
