# CONTINUAR

frutas={
    "frutas":[]
}
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
                val=input("Que valor lleva esta fruta?: ")
                frutas[fru]=val 
            case 2:
                frutas=#ccc
            case 3:
                fru_borrar=input("")
    except Exception as e:
        print(f"Print error {e}")