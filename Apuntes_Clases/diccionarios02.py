#Continuar con github del profe  repaso_prueba 003D

juegos={
    1:{
        "Nombre":"Metroid",
        "Precio":5000,
        "Code":"MMdd2023"
    },
    2:{
        "Nombre":"Pikmin 4",
        "Precio":7600,
        "Code":"pKMn2022"
    }
}

# nombre=input("Ingrese el nombre del juego: ")
# precio=int(input("Precio del juego $"))
# code=input("Ingrese código: ")

# juegos[4]={
#     "Nombre":nombre,
#     "Precio":precio,
#     "Code":code
# }
# for j, datos in juegos.items():
#     print(j, datos)

# print(juegos[2]["Precio"]) #Dentro de juegos, 2do key muestra valor "Precio"
def mostrar(dic):
    for j, datos in juegos.items():
                    print(j, datos)
def borrar(dic):
     mostrar(dic)
     borrar=int(input("Que elemento desea eliminar: "))
     del juegos[borrar]
def actualizar(dic):
     mostrar(dic)
     act=int(input("Seleccione juego a actualizar: "))
     while True:
        print('''
              1.- Nombre
              2.- Precio
              3.- Código
              4.- Salir
            ''')
        op=int(input("Que dato va a actualizar?: "))
        match op:
            case 1:
                n=input("Ingrese nuevo nombre: ")
                dic[act]["Nombre"]=n
            case 2:
                  #upudpate precio
            case 4:
                break
            case _:
                  print("Iválido")      
while True:
    try:
        print('''
              1.- Agregar artcículo
              2.- Mostrar productos
              3.- Actualizar artículo
              4.- Borrar productos
              5.- Salir
              ''')
        opc=int(input("Seleccione una opción: "))
        match opc:
            case 1:
                nombre=input("Ingrese el nombre del juego: ")
                precio=int(input("Precio del juego $"))
                code=input("Ingrese código: ")
                largo=len(juegos)
                juegos[largo+1]={
                "Nombre":nombre,
                "Precio":precio,
                "Code":code
                }
            case 2:
                mostrar(juegos)                
            case 3:
                actualizar(juegos)
            case 4:
                borrar(juegos)
            case 5:
                break
            case _:
                print("Inválido")
    except Exception as e:
        print("error",e)