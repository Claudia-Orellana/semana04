cola = ['Sofia', 'Mateo', 'Valeria']
while True:
    menu = '(1) Registrar estudiante regular\n(2) Registrar estudiante prioritario\n(3) Cancelar una solicitud\n(4) Atender al siguiente estudiante\n(5) Consultar la cola\n(6) Cerrar el sistema'
    print(menu)
    select = int(input('Ingresa el numero de la opcion: '))
    if select == 1:
        Nombre_estudiante = input(
            'Ingresa el nombre del estudiante: ').capitalize()
        if Nombre_estudiante == '':
            print('Su nombre esta vacio')
        elif Nombre_estudiante in cola:
            print('El estudiante ya fue registrado')
        else:
            cola.append(Nombre_estudiante)
            print('El estudiante se ha agregado con exito')
            print(cola)
    elif select == 2:
        Nombre_estudiante = input(
            'Ingresa el nombre del estudiante: ').capitalize()
        if Nombre_estudiante == '':
            print('Su nombre esta vacio')
        elif Nombre_estudiante in cola:
            print('El estudiante ya fue registrado')
        else:
            cola.insert(0, Nombre_estudiante)
            print('El estudiante se ha agregado con exito')
            print(cola)
    elif select == 3:
        Nombre_estudiante = input(
            'Ingresa el nombre del estudiante: ').capitalize()
        if Nombre_estudiante == '':
            print('Su nombre esta vacio')
        elif Nombre_estudiante not in cola:
            print('El estudiante no se encuentra en la cola')
        else:
            cola.remove(Nombre_estudiante)
            print('La solicitud ha sido eliminada')
    elif select == 4:
        if cola == []:
            print('La cola esta vacia')
        else:
            Nombre_estudiante = cola.pop(0)
            print(f'El estudiante {Nombre_estudiante} esta siendo atendido')
            print('El estudiante ha sido eliminado de la cola')
    elif select == 5:
        print(f'El orden actual de la cola es: {cola}')
    elif select == 6:
        print('Gracias por usar nuestro sistema')
        break
