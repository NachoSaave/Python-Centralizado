while True:
    try:
        num=int(input("Ingrese un número entre 0 y 100"))
        if num<0 or num>100:
            print("Fuera de rango")
        else:
            break
    except ValueError:
        print("No se permiten valores fuera de tipo integral")