#gestion de mascotas -> veterinaria
#todos los elemenos del sistema de gestion estaran mediante funciones
#hay que crear validaciones con los menus
#operaciones logicas de decisiones
#se trabaja con  diccionarios y listas

#funciones
def mostrar_menu():
    print("====== MENU PRINCIPAL ======")
    print("1.- agregar mascota")
    print("2.- buscar mascota")
    print("3.- Eliminar mascota")
    print("4.- marcar como vacunada")
    print("5.- mostrar mascotas")
    print("6.- Salir")
    print("===========================")
    print("")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Debe selecionar una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero")
    return opcion


#codigo principal
#declaro la lista de mascotas
coleccion_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()