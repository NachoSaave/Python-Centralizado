agenda={}
def validar_rut(rut):
    digit=0
    space=0
    if len(rut)>9:
        return False
    for i in rut:
        if i==" ":
            space+=1
        elif i.isdigit():
            digit+=1
    if digit>=9 and space==0:
        return True
    else:
        return False
    
#Declarar posicionamiento dentro del diccionario
if agenda:
    largo=max(agenda.keys())+1
else:
    largo=1

def agregar(dic):
    while True:
        try:
            nombre=input("Ingrese un nuevo nombre: ")
            rut=input("Ingrese su RUT: ")
            validar_rut(rut)
            telefono=(input("Ingrese un nuevo número +56"))
            if len(telefono)>9:
                print("Intente de nuevo con un número válido")
                return
            else:
                agenda[largo]={
                    'Nombre':nombre,
                    'RUT':rut,
                    'Telefono':telefono
                }

        except Exception as er:
            print(er)

# def buscar(dic):

# def borrar(dic):

# def listar(dic):

def menu(dic):
    while True:
        try:
            op=int(input('''-- MENU PRINCIPAL --
                1.- Agregar
                2.- Buscar
                3.- Borrar
                4.- Listar
                5.- Salir
                    Ingrese su opción: 
                '''))
            match op:
                case 1:
                    agregar(dic)
                case 5:
                    print("Terminando sistema")
                    exit()
                case _:
                    print("Debe intentar de nuevo")
        except Exception as e:
            print(e)

menu(agenda)