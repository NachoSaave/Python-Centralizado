import time
nombres=[]
apellidos=[]
while True:
    print('''
        1.- Ingresar un nombre
        2.- Buscar nombre
        3.- Mostrar lista
        4.- Salir
          ''')
    op=int(input("Seleccione una opción: "))
    match op:
        case 1:
            nom=input("Ingrese un nombre: ")
            nombres.append(nom)
            ape=input("Ingrese un apellido: ")
            apellidos.append(ape)
            print(nombres, apellidos)
        case 2:
            busca=input("Que nombre desea buscar?: ")
            time.sleep(1)
            if busca in nombres:
                print(f"El nombre {busca} existe en la lista")
            else:
                print("El nombre no existe en la lista")
        case 3:
            cont=1
            # for nombre in nombres and apellidos:
            #     print(f"{cont}.- {nombres[cont-1]} {apellidos[cont-1]}")
            #     cont+=1
            for i in range(len(nombres)):
                print(f"{i+1}.- {nombres[i]} {apellidos[i]}")
                cont+=1
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opción no válida")
