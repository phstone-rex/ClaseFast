#gestion de mascotas -> veterinaria
#todos los elemenos del sistema de gestion estaran mediante funciones
#hay que crear validaciones con los menus
#operaciones logicas de decisiones
#se trabaja con  diccionarios y listas

#funciones
#validaciones
def validar_nombre(name):
    #una funcion en python que elimina los espacios al inicio o al final de un steing y si queda vacia devuleve un false
    return name.strip() != "" #retorna true si es valido - false si es invalido
def validar_especie(especie):
    #validar que es perro, gato o ave, solamente (sin diferenciar mausculas o minusculas)
    especies_validas = ["perro", "gato", "ave"]
    return especie.strip().lower() in especies_validas
def validar_edad(edad):
    #que sean numeros y mayor a cero
    #isdigit() --> revusa q el string contenga solo digitos (no negativo, no decimal)
    return edad.isdigit() and int(edad) > 0



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

#opcion1
def agregar_mascota(lista):
    nombre = input("Ingrese el nombre de la mascota: ")
    #llamar la funcion que valida el nombre para mostrar el mensaje
    correcto = validar_nombre(nombre)
    if not correcto:
        print("El nombre no puede estar vacia")
        return
    
    #llamar la fbciuonb pqe valida la especie para mostrar el mensaje
    especie = input("Ingrese la especie de la mascota (Perro, Gato o Ave): ")
    correcto = validar_especie(especie)
    if not correcto:
        print("La especie solo puede ser perro, gato o ave")
        return
    
    edad = input("Ingrese la edad de la mascota: ") #en otro lado vamos a configurar para que haya int
    correcto = validar_edad(edad)
    if not correcto:
        print("La edad debe ser un numero entero mayor a cero")
        return
    #aqui agreggo al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    #agrego a la lista
    lista.append(mascota)
    print("Mascota agregada correctamente")

#codigo principal
#declaro la lista de mascotas
lista_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()

    if op == 1:
        agregar_mascota(lista_mascotas)
    elif op == 2:
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sistema")

