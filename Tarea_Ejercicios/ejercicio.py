def clave():
    clave=3344
    password=int(input("Ingrese su clave: "))
    while clave!=password:
        print("ERROR! Clave Invalida")
        password=int(input("Ingrese su clave nuevamente"))
    print("Bienvenido al sistema")

clave()