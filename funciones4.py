#funciones
def conversion_notas(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) + 1
    return round(nota,1)

#codigo principal
while True:
    try:
        p = float(input("ingresa la nota del estudiante: "))
        if p < 0:
            print("Debe ser una nota positiva")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")

while True:
    try:
        pt = float(input("Ingrese la nota total de la evaluacion: "))
        if pt < 0:
            print("Debe ser una nota total positiva")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")

#llamar a la funcion para enviar datos y mostrar la nota convertida

calif = conversion_notas(p,pt)
print(f"La nota Chilena es; {calif}")

