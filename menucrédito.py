# Menu de trajeta e crédito
# POR HACER/COMPLETAR
import time
deuda=0
saldo=100000
def pagar():
    global saldo, deuda
    print(f"Tiene un monto pendiente de ${deuda}")
    deuda=int(input("Ingrese el monto que quiere cancelar: $"))
    if deuda>saldo:
        print("Cancelando pago...")
        saldo-deuda
        time.sleep(1)
        opcompra=int(input("Le gustaría hacer otro pago? 1- Si. 2- No."))
        match opcompra:
            case 1:
                pagar()
            case 2:
                print("Cancelando pago...")
                time.sleep(1)
                saldo-deuda
   
def comprar():
    global saldo, deuda
    try:
        deuda=int(input("Ingrese el monto que va a comprar: $"))
    except ValueError as Error:
        print("Debe ingresar un monto válido")
        if deuda<0:
            print("Debe ingresar un monto mayor a $0")
        elif deuda>saldo:
            print("No tiene suficiente dinero en su cuenta")
        else:
            print("Debe ingresar un valor válido")

def menu():
    global deuda, saldo
    while True:
        while True:
            try:
                op=int(input('''
                        Seleccione una opción
                        1.- Pagar
                        2.- Comprar
                        3.- Salir
                        '''))
                break
            except Exception:
                print("Solo números enteros")
        match op:
            case 1:
                print("Yendo a pagar...")
                time.sleep(1)
                pagar()
            case 2:
                print("Yendo de comprar...")
                time.sleep(1)
                comprar()
            case 3:
                print("Saliendo...")
                break
            case _:
                print("Opción inválida")

menu()