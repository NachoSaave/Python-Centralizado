# CONTINUAR

frutas=[
    {}
]
while True:
    try: 
        opc=int(input('''
        1.- Ingresar fruta y precio
        2.- Actualizar precio
        3.- Borrar fruta y precio
        4.- Mostrar todas la frutas y precios
        5.- Salir'''))
        match opc:
            case 1:
                fru=input("Que fruta desea agregar?: ")
                val=input("Que valor lleva esta fruta? $")
                frutas.insert(0,{"Fruta":fru}, {"Precio":val})
            case 2:
                try:
                    print("Frutas y su valor")
                    for i in range(len(frutas)):
                        print(f"{[i+1]} {frutas[i]}")
                    actualizar=int(input("Ingrese el número de la fruta que desea actualizar"))
                    frutas[actualizar-1]["Fruta"]=input("Ingrese el nuevo nombre de la fruta: ")
                    frutas[actualizar-1]["Precio"]=int(input("Ingrese el nuevo valor $"))
                    print("Elementos actualizados correctamente")
                except Exception as er:
                    print(e)
            case 3:
                try:
                    print("Frutas y su valor")
                    for i in range(len(frutas)):
                        print(f"{[i+1]} {frutas[i]}")
                    borrar=int(input("Ingrese el número de la fruta que desea borrar"))
                    print(f"El producto {borrar} se ha eliminado exitosamente")
                    frutas.pop(borrar-1)
                except Exception as err:
                    print(err)
            case 4:
                print("frutas y precios")
                for i in range(len(frutas)):
                    print(f"{[i+1]} {frutas[i]}")
            case 5:
                print("Saliendo...")
                break
    except Exception as e:
        print(f"Print error {e}")