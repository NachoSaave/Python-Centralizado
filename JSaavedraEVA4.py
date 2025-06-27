entradas={

}
largo=1
def validarCodigo(codigo):
    minus=0
    digit=0
    if len(codigo)!=6:
        return False
    for i in codigo:
        if i.islower():
            minus+=1
        elif i.isdigit():
            digit+=1
    if minus>=1 and digit>=1:
        return True
    else:
        return False
def comprar(dic):
    global largo
    nombre=input("Ingrese su nombre: ")
    if nombre not in entradas:
        print("Nombre confirmado")
    else:
        print("Nombre ya inscrito")
    tipoEntrada=input("Que tipo de entrada desea llevar? (G o V): ")
    if tipoEntrada=='G' or tipoEntrada=='V':
        print("Entrada comprada exitosamente")
    else:
        print("Intente de nuevo")
    codigo=input("Entre su código de confirmación: ")
    if not validarCodigo(codigo):
        print("Código inválido. Compra no realizada.")
        return
    entradas[largo]={
        'Nombre':nombre,
        'Tipo':tipoEntrada,
        'Codigo':codigo
    }
    largo+1
def consultar(dic):
    nombreBuscar=input("Ingrese el nombre que desea buscar: ")
    print("Compras encontradas:")
    encontrado=False
    for indice, detalles in entradas.items():
        if detalles['Nombre']==nombreBuscar:
            print(f"{indice}: Tipo: {detalles['Tipo']}, Código: {detalles['Codigo']}")
            encontrado=True
    if not encontrado:
        print("No se encontraron compras para ese nombre.")
def cancelar(dic):
    op=int(input("Seleccione la posición de la compra que desea borrar: "))
    if op in dic:
        del dic[op]
        print("Compra cancelada exitosamente.")
    else:
        print("No se encontró una compra en esa posición.")

    

def salir():
    print("Terminando programa...")
    exit()

while True:
    try:    
        print('''
                    ----0---- MENU PRINCIPAL ----0----
                    1.- Comprar entrada
                    2.- Consultar Comprador
                    3.- Cancelar compra
                    4.- Salir
                    ''')
        opc=int(input("Seleccione una opción: "))
        match opc:
            case 1:
                comprar(entradas)
            case 2:
                consultar(entradas)
            case 3:
                cancelar(entradas)
            case 4:
                salir()
            case _:
                print("Debe ingresar una ocpión valida!!")
    except Exception as e:
        print(e)