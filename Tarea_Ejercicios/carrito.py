precio=0
nombre=input("Ingrese su nombre")
def super():
    while True:
        op=int(input('''Que desea hacer?
                    1.- Ir a cereales
                    2.- Ir a bebestibles
                    3.- Ir a snacks
                    4.- Pagar'''))
        match op:
            case 1:
                print("Yendo al pasillo de cereales...")
                cereales()
            case 2:
                print("Yendo al pasillo de bebestibles")
                bebestibles()
            case 3:
                print("Yendo al pasillo de snacks")
                snacks()
            case 4:
                print(f"Pagando... El valor neto de su boleta es {precio} (+ IVA = {round(precio*1.19)}). Hasta luego, {nombre}!")
                break
            case _:
                print("Ingrese una opción válida")
def cereales():
    global precio
    opcereales=int(input('''Que cereal llevará?
                         1.- Milo ($2670)
                         2.- Chocapic ($2990)
                         3.- Zucaritas ($3590)
                         4.- Trix ($4490)
                         5.- Avena quaker ($4090)
                         6.- Salir'''))
    match opcereales:
        case 1:
            print("Lleva milo")
            precio=precio+2670
        case 2:
            print("Lleva chocapic")
            precio=precio+2990
        case 3:
            print("Lleva zucaritas")
            precio=precio+3590
        case 4:
            print("Lleva trix")
            precio=precio+4490
        case 5:
            print("Lleva avena quaker")
            precio=precio+4090
        case 6:
            print("Saliendo...")
            super()
def snacks():
    global precio
    opsnacks=int(input('''Que snack llevará?
                         1.- Doritos ($3490)
                         2.- Papas americanas ($2630)
                         3.- Papas en tarro ($1790)
                         4.- Ramitas ($2239)
                         5.- Tostitos ($3999)
                         6.- Salir'''))
    match opsnacks:
        case 1:
            print("Lleva doritos")
            precio=precio+3490
        case 2:
            print("Lleva papas americanas")
            precio=precio+2630
        case 3:
            print("Lleva papas en tarro")
            precio=precio+1790
        case 4:
            print("Lleva ramitas")  
            precio=precio+2239
        case 5:
            print("Lleva tostitos")
            precio=precio+3999
        case 6:
            print("Saliendo...")
            super()
def bebestibles():
    global precio
    opbebestibles=int(input('''Que bebestible llevará?
                         1.- Cocacola 2L ($2500)
                         2.- Fanta 2L ($2570)
                         3.- Sprite 2L ($2590)
                         4.- Pepsi 2L ($2190)
                         5.- Gatorade 1L ($1000)
                         6.- Salir'''))
    match opbebestibles:
        case 1:
            print("Lleva cocacola")
            precio=precio+2500
        case 2:
            print("Lleva fanta")
            precio=precio+2570
        case 3:
            print("Lleva sprite")
            precio=precio+2590
        case 4:
            print("Lleva pepsi")
            precio=precio+2190
        case 5:
            print("Lleva gatorade")
            precio=precio+1000
        case 6:
            print("Saliendo...")
            super()
    
super()