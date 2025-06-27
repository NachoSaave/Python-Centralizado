autos={
    
}
largo=1
def validar_patente(patente):
    minus=0
    digit=0
    if len(patente)!=6:
        return False
    for i in patente:
        if i.islower():
            minus+=1
        elif i.isdigit():
            digit+=1
    if minus>=4 and digit>=2:
        return True
    else:
        return False
def mostrar():
    for indice, detalles in autos.items():
        print(indice, detalles)
def agregar():
    global largo
    iauto=input("Que marca el auto ")
    iaño=int(input("Que año es "))
    ipatente=input("Patente ")
    if validar_patente(ipatente):
        print("Patente válida")
    else:
        print("Patente inválida, debe tener 4 letras minúsculas y 2 dígitos")
        return
    itipo=input("Tipo de auto (A- Auto C- Camión M- Moto): ")
    if itipo in ['A','C','M']:
        autos[largo]={
            'marca': iauto,
            'año': iaño,
            'patente': ipatente,
            'tipo': itipo
        }
        largo+=1   
    else:
        print("Tipo de auto no válido, debe ser A, C o M")
def borrar():
    mostrar()
    borrar=int(input("Seleccione el vehículo que desea borrar: "))
    if borrar in autos:
        del autos[borrar]
        print("Vehículo borrado")
    else:
        print("Vehículo no encontrado")
def estadisticas():
    print(f"Último vehículo agregado: {(autos[list(autos.keys())[-1]])}")
    print("El total de vehículos es: ", len(autos))
def actualizar():
    mostrar()
    actulizar=int(input("Seleccione cuál vehículo desea actualizar: "))
    if actulizar in autos:
        nuevaMarca=input("Nueva marca: ")
        nuevoAño=int(input("Nuevo año: "))
        nuevaPatente=input("Nueva patente: ")
        nuevoTipo=input("Nuevo tipo de auto (A- Auto C- Camión M- Moto): ")
        autos[actulizar] = {
            'marca': nuevaMarca,
            'año': nuevoAño,
            'patente': nuevaPatente,
            'tipo': nuevoTipo
        }
    else:
        print("No encontrado, intente de nuevo")
def salir():
    print("Saliendo del programa...")
    exit()
while True:
    try:
        print('''
              1.- Agregar
              2.- Mostrar
              3.- Borrar
              4.- Estádisticas
              5.- Actualizar datos
              6.- Salir
              ''')
        opc=int(input("Seleccione una opción: "))
        match opc:
            case 1:
                agregar()
            case 2:
                mostrar()
            case 3:
                borrar()
            case 4:
                estadisticas()
            case 5:
                actualizar()
            case 6:
                salir()
            case _:
                print("Opción no válida")
    except Exception as e:
        print(e)