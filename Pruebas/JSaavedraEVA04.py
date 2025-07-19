import time
import sys
entradas={
    1:{
        'Nombre':"Chris",
        'Tipo':"G",
        'Codigo':"Kodig9"
    }
}
  # Código para validación de existencia en diccionario
# name="Chris"
# for k, v in entradas.items():
#     if v["Nombre"]==nombre:
#         print("Existe")
#     else:
#         print("No existe")
#     print(v["Nombre"])
#     print(k,v)

if entradas:
    largo=max(entradas.keys())+1
else:
    largo=1

def validarCodigo(codigo):
    mayus=0
    digit=0
    space=0
    if len(codigo)<6:
        return False
    for i in codigo:
        if i.isupper():
            mayus+=1
        elif i==" ":
            space+=1
        elif i.isdigit():
            digit+=1
    if mayus>=1 and digit>=1 and space==0:
        return True
    else:
        return False

def comprar(dic):
    global largo
    while True:
        nombre=input("Ingrese su nombre: ") #Hay que aplicar elemento en línea 9-16
        for k, v in entradas.items():
            if v["Nombre"]==nombre:
                print("Este nombre ya está inscrito, debe intentar otro diferente")
                return
            else:
                time.sleep(1)
                print(f"Nombre {nombre} inscrito exitosamente!")
                time.sleep(1)
        break
    while True:
        tipoEntrada=input("Que tipo de entrada desea llevar? (G o V): ")
        if tipoEntrada=='G' or tipoEntrada=='V':
            time.sleep(1)
            break
        else:
            print("Intente de nuevo")
    while True:
        codigo=input("Entre su código de confirmación: ")
        time.sleep(1)
        if not validarCodigo(codigo):
            print("Código inválido. Compra no realizada.")
            return
        else:
            print("Código verificado")
            entradas[largo]={
                'Nombre':nombre,
                'Tipo':tipoEntrada,
                'Codigo':codigo
            }
            largo+1
            time.sleep(1)
            break

def consultar(dic):
    nombreBuscar=input("Ingrese el nombre que desea buscar: ")
    time.sleep(3)
    print("Compras encontradas:")
    time.sleep(1)
    encontrado=False
    for indice, detalles in entradas.items():
        if detalles['Nombre']==nombreBuscar:
            print(f"{indice}: Tipo: {detalles['Tipo']}, Código: {detalles['Codigo']}")
            encontrado=True
    if not encontrado:
        print("No se encontraron compras para ese nombre.")

def cancelar(dic):
    op=int(input("Seleccione la posición de la compra que desea borrar (Debe consultar su nombre antes, para poder ver su posición): "))
    time.sleep(1)
    if op in dic:
        del dic[op]
        print("Compra cancelada exitosamente.")
    else:
        print("No se encontró una compra en esa posición.")

def salir():
    print("Terminando programa...")
    time.sleep(3)
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