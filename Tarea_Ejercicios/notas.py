notas=[7.0, 3.7, 5.9]
import time
promedio=0
while True:
    try:
        opc=int(input('''Programa de manejo de notas
                    1.- Ingresar nota
                    2.- Borrar nota
                    3.- Mostrar notas
                    4.- Sacar promedio
                    5.- Limpiar todas las notas
                    6.- Salir
                    '''))
        match opc:
            case 1:
                ingreso_nota=float(input("Ingrese la nota: "))
                notas.append(ingreso_nota)
            case 2:
                for i in range(len(notas)):
                    print(f"{i+1}.- {notas[i]}")
                borrar_nota=int(input("Ingrese la posición de la nota que desea eliminar: "))-1
                notas.pop(borrar_nota)
            case 3:
                for i in range(len(notas)):                    
                    print(f"{i+1}.- {notas[i]}")
            case 4:
                suma=0
                for j in range(len(notas)):
                    print(f"{j+1}.- {notas[j]}")
                    suma+=notas[j]
                promedio=suma/len(notas)
                print(f"El promedio de las notas es {round(promedio,1)}")
                notas.sort()
                print(f"Las nota mayor es un {notas[-1]}")
                print(f"La menor nota es un {notas[0]}")
            case 5:
                print("Limpiando todas la notas...")
                time.sleep(1)
                notas=[]
            case 6:
                print("Saliendo del sistema...")
                break
            case _:
                print("Ingrese una opción válida")
    except Exception as lol:
            print("Opción inválida: ",lol)      