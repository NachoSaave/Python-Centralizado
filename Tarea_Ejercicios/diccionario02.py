# productos=[
#     {
#     "Nombre":"Leon",
#     "precio": 200
#      },
#     {
#     "Nombre":"Goma",
#     "precio": 400
#      },
#     {
#     "Nombre":"Estuche",
#     "precio": 1600
#      }
# ]
# # print(f"El pecio de la {productos[1]["Nombre"]} es {productos[1]["precio"]}")
# for producto in productos:
#     print(f"El precio de {producto["Nombre"]} es {producto["precio"]}")



#CONTINUAR
import time
productos=[
    {}
]
while True:
    try:
        opc=int(input('''
              1.- Agregar artcículo
              2.- Borrar artículo
              3.- Actualizar artículo
              4.- Mostrar productos
              5.- Salir
              '''))
        match opc:
            case 1:
                art=input("Ingrese el nombre del producto: ")
                precio=int(input("Cuál es el precio del producto $"))
                productos.insert(0,{"Nombre":art, "Precio":precio})
            case 2:
                try:
                    for i in range(len(productos)):
                        print(f"{i+1}.- {productos[i]}")
                    borrar=int(input("Ingrese el número del producto que desea eliminar"))
                    print(f"El producto {borrar} se ha eliminado de la lista")
                    productos.pop(borrar-1)
                    print("Producto borrado exitosamente")
                    time.sleep(1)
                except Exception as er:
                    print(e)
            case 3:
                try:
                    print("Productos y precios")
                    for i in range(len(productos)):
                        print(f"{[i+1]} {productos[i]}")
                    actualizar=int(input("Ingrese el número del producto que quiere actualizar"))
                    productos[actualizar-1]["Nombre"]=input("Ingrese el nuevo nombre del producto que va a actualizar")
                    productos[actualizar-1]["Precio"]=int(input("Ingrese el nuevo precio del artículo actualizado"))
                    print("Elemento actualizado correctamente")
                    time.sleep(1)
                except Exception as err:    
                    print(err)
            case 4:
                print("Productos y precios")
                for i in range(len(productos)):
                    print(f"{[i+1]} {productos[i]}")
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción inválida")
    except Exception as e:
        print("Error",e)
        
