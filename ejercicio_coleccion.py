# productos = []
# for i in range(5):
#     nombre_producto=input("Ingrese el nombre del producto: ")
#     productos.append(nombre_producto)
# print(productos)
import time
from os import system
productos = []
while True:
    try:
        opc=int(input('''Que desea hacer?
                      1.- Agregar productos
                      2.- Eliminar productos
                      3.- Mostrar carrito
                      4.- Salir'''))
    except Exception:
        print("Ingrese valor correspondiente")
    match opc:
        case 1:
            nombre_productos=input("Ingrese el nombre del producto que desea agregar: ")
            productos.append(nombre_productos)
            print(f"{nombre_productos} agregado a la lista de productos")
            system("cls")
        case 2:
            cont=1
            for i in productos:
                print(f"{cont}.- {i}")
                cont+=1
            aux=int(input("Ingrese el nombre del producto que desea eliminar: "))-1
            productos.pop(aux)
            print(f"{nombre_productos} eliminado de la lista de productos")
            system("cls")
        case 3:
            print("Mostrando productos...")
            time.sleep(1)
            cont=1
            for i in productos:
                print(f"{cont}.- {i}")
                cont+=1
        case 4:
            print("Saliendo...")
            time.sleep(1)
            break
        case _:
            print("Ingrese un valor correspondiente")
