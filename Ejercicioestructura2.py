import numpy as np

def seleccion_menu():
    while True:
        opciones = input("Eliga una opción del menu.\n")
        if opciones.isdigit():
            opciones = int(opciones)
            return opciones
        else:
            print("Ingrese una opción válida\n")
            continue

def menu():
    print("SERVICIO DE ATENCIÓN MÉDICA DE URGENCIAS")
    print("\n˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ \n࣪")
    print("1- Ingresar ficha del paciente.")
    print("2- Buscar ficha por RUT.")
    print("3- Buscar medicamentos por RUT.")
    print("4- Eliminar ficha del paciente.")
    print("5- Listar pacientes atendidos")
    print("6- Salir")
    print("\n˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ \n࣪")
    
def seleccion_rut():
    while True:
        try:
            rut = str(input("Ingrese rut con guion: "))
            assert len(rut) == 10 and rut.find("-") == 8
            break
        except AssertionError:
            print("ERROR: Debe ingresar el RUT sin puntos y con el guion antes del dígito verificador.")
    return rut

def pacientesorden(i, j, pac):
    if j == 0:
        print("Nombre:", pac[i, j])
    elif j == 1:
        print("Rut:", pac[i, j])
    elif j == 2:
        print("Edad:", pac[i, j])
    elif j == 3:
        print("Sexo:", pac[i, j])
    elif j == 4:
        print("Teléfono:", pac[i, j])
    elif j == 5:
        print("Diagnóstico:", pac[i, j])
    elif j == 6:
        print("Medicamentos recetados:", pac[i, j])

pac = np.empty([50, 7], dtype="object")
f = 0

while True:
    menu()
    opcion = seleccion_menu()
    
    if opcion == 1:
        for i in range(50):
            if pac[i, 1] is None:
                print("Ingrese el nombre del paciente")
                pac[i, 0] = input()
                x = seleccion_rut()
                pac[i, 1] = x
                print("Ingrese la edad del paciente")
                pac[i, 2] = input()
                print("Ingrese el sexo del paciente")
                pac[i, 3] = input()
                print("Ingrese el fono del paciente")
                pac[i, 4] = input()
                print("Ingrese el diagnóstico del paciente")
                pac[i, 5] = input()
                print("Ingrese medicamentos recetados del paciente")
                pac[i, 6] = input()
                f += 1
                print("Paciente ingresado con éxito")
                break
        else:
            print("No hay espacio disponible para más pacientes")
    
    elif opcion == 2:
        x = seleccion_rut()
        for i in range(50):
            if pac[i, 1] == x:
                print("Paciente encontrado, sus datos son los siguientes:")
                for j in range(7):
                    pacientesorden(i, j, pac)
                break
        else:
            print("Paciente no encontrado")
    
    elif opcion == 3:
        print("Ingrese el rut del paciente a buscar")
        x = seleccion_rut()
        for i in range(50):
            if pac[i, 1] == x:
                print("Paciente encontrado, los medicamentos recetados son los siguientes:")
                print(pac[i, 6])
                break
        else:
            print("Paciente no encontrado")
    
    elif opcion == 4:
        print("Ingrese el rut del paciente a eliminar")
        x = seleccion_rut()
        for i in range(50):
            if pac[i, 1] == x:
                pac[i] = np.empty(7, dtype="object")  
                print("Paciente eliminado con éxito")
                break
        else:
            print("Paciente no encontrado")
    
    elif opcion == 5:
        for i in range(f):
            print("\n˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ ࣪˖ \n࣪")
            print("Paciente:")
            for j in range(7):
                pacientesorden(i, j, pac)
    
    elif opcion == 6:
        break
    
    else:
        print("Ingrese una opción válida")
