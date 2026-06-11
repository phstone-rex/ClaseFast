#funciones
def mostrar_encabezado():
    print("=================")
    print("|| Sistema de admision Escolar ||")
    print("=================")

def solicitar_datos():
    estudiantes = {}
    estudiantes["rut"] = input("ingrese el rut del estudiante: ")
    estudiantes["nombre"] = input("Ingrese el nombre del estudiante: ")
    estudiantes["carrera"] = input("Ingrese el nombre de la carrera: ")
    while True:
        try:
            estudiantes["semestre"] = int(input("Ingrese el semestre que cursa: "))
            if estudiantes["semestre"] < 1 or estudiantes["semestre"] > 4:
                print("Debe ser del 1 al 4")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero entero")
    return estudiantes

def mostrar_datos(alumnos):
    print(f"Nombre del estudiante: {alumnos["nombre"]}")
    print(f"Rut del estudiante: {alumnos["rut"]}")
    print(f"Carrera del estudiante: {alumnos["carrera"]}")
    print(f"Semestre del estudiante: {alumnos["semestre"]}")
#codigo principal
datos = solicitar_datos()
#imprimir el encabezado
mostrar_encabezado()
mostrar_datos(datos)
