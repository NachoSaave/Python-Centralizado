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

# '''
# el codigo debe tener 2 mayusculas,
# 2 minusculas y 4 numeros
# '''

def mostrar_juegos(dic):
    for j, datos in dic.items():
        print(j, datos)

def valida_code(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4 :
        print("El codigo está bien escrito")
        return True
    else:
        print("El codigo está mal escrito")
        return False
def borrar(dic):
     mostrar(dic)
     borrar=int(input("Que elemento desea eliminar: "))
     del juegos[borrar]
def act_juegos(dic):
    mostrar(dic)
    act=int(input("Seleccione el juego a actulizar: "))
    while True:
        print('''1.- Nombre
                2.- Precio
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                dic[act]["nombre"]=n
            case 2:
                n=int(input("ingrese la nueva raza"))
                dic[act]["precio"]=n
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_code(n):
                    dic[act]["codigo"]=n
                else:
                    print("el parametro del codigo no es correcto")
                    print('''
                    el codigo debe tener, 2 mayusculas, 
                    2 minusculas y 4 numeros ''')
            case 4:
                break
            case _:
                    print("Opcion invalida")  
def ingresar(dic):
    while True:
        nombre=input("Ingrese el nombre del juego: ")
        if valida_nombre(nombre):
            break
        else:
            print("nombre invalido, intenta nuevamente")
            nombre=input("Ingrese el nombre del juego: ")
    precio=int(input("Ingrese el precio: "))
    code=input("Ingres el codigo: ")
    if valida_code(code):
        largo=list(dic.keys())[-1]
        dic[largo+1]={
                "nombre":nombre,
                "precio": precio,
                "code":code
            }
    else:
        print("el codigo es invalido, intenta de nuevo")

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
                ingresar(juego)
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