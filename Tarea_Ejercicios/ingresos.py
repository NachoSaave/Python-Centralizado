credito=0
ingresos=int(input('''Dentro de que rango están sus ingresos?
                   1.- Arriba de $500.000 bajo de $1.000.000
                   2.- Arriba de $1.000.001 bajo de $1.500.000
                   3.- Arriba de $1.500.000
'''))
match ingresos:
    case 1:
        credito+=300000
        print(f"Su crédito equivale a {credito}")
    case 2:
        credito+=650000
        print(f"Su credito equivale a {credito}")
    case 3:
        credito+=1000000
        print(f"Su credito equivale a {credito}")
educacion=int(input('''Que nivel de educación completada tiene?
                    1.- Educación básica
                    2.- Educación media
                    3.- Educación superior
'''))
match educacion:
    case 1:
        credito*=1
        print(f"Su credito equivale a {credito}")
    case 2:
        credito*=1.3
        print(f"Su credito equivale a {credito}")
    case 3:
        credito*=1.5
        print(f"Su credito equivale a {credito}")
nacionalidad=int(input('''Seleccione su nacionalidad
                       1.- Chilena
                       2.- Extrajero
'''))
match nacionalidad:
    case 1:
        credito+=300000
        print(f"Su credito final equivale a {credito}")
    case 2: 
        print(f"Su credito final equivale a {credito}")