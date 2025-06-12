# Algo no sirve...

productos=[]
precio=[]
carrito=[]
total=0
while True:
    opc=int(input('''**Bienvenido a carrito version 03**
                Que desea hacer?
                1.- Agregar producto
                2.- Comprar
                3.- Crear boleta
                4.- Salir
                '''))
    match opc:
        case 1:
            try:
                agregar=input("Que producto desea agregar?: ")
                precio_producto=int(input("Ingrese valor del producto: "))
                productos.append(agregar)
                precio.append(precio)
                print(f"Usted agregó {agregar}: {precio_producto}")
            except Exception as e:
                print(f"Error {e}")
        case 2:
            try:
                for i in range(len(productos)):
                    print(f"{i+1}.- {productos[i]}: {precio[i]}")
                comprar=int(input("Seleccione el número del productro que desea llevar: "))
                carrito.append(comprar)
                print(f"Usted agregó {productos[comprar]} al carrito")
            except Exception as e2:
                print(f"Error {e2}")
        case 3:
            print("- - Boleta - -")
            for indice in carrito:
                print(f"{productos[indice]}-- {precio[indice]}")
                total+=precio[indice]
                print("--------------------")
                print(f"El total a pagar es {total}")
        case 4:
            print("Usted está saliendo del sistema Carrito Version 03, hasta luego!")
            break
        case _:
            print("Ingrese una opción válida")

